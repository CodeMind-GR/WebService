import requests
from datetime import datetime
from os import environ as env
from zoneinfo import ZoneInfo

import boto3
import streamlit as st
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Streamlit 페이지 설정
st.set_page_config(page_title="CodeMind Project", layout="wide")

# DynamoDB에 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('User')

# auth 인증 후 access token 및 user info 설정
token = st.query_params.get_all("token")
email = st.query_params.get_all("email")
name = st.query_params.get_all("name")

auth0_app_url = env.get("AUTH0_APP_URL")
hf_model_api_server_url = env.get("HF_MODEL_API_SERVER_URL")


def save_email_to_dynamodb(email, name):
    current_time = datetime.now(ZoneInfo("Asia/Seoul")).isoformat()
    response = table.put_item(
        Item={
            'user_id': email,
            'nick_name': name,
            'last_login': current_time
        }
    )
    return response


def generate_response(prompt):
    response = requests.post(hf_model_api_server_url, json={"text": prompt})
    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        return "Error: " + response.text


def main():
    if token and email:
        save_email_to_dynamodb(email[0], name[0])
        # 토큰이 있는 경우, 사용자가 로그인한 것으로 간주하고 채팅 페이지를 표시
        display_chat_page()
    else:
        # 토큰이 없는 경우, 홈 페이지를 표시
        display_home_page()


def display_home_page():
    st.title("Welcome to Our ChatGPT-like Web App")
    st.write("""
        This is a simple web application using Streamlit to demonstrate a ChatGPT-like interface.
        You can interact with an AI model, ask questions, and get responses in real-time.
    """)
    auth_url = auth0_app_url + "/login"  # 외부 인증 서버의 URL
    st.markdown(f'<a href="{auth_url}"><button>Login to Chat</button></a>', unsafe_allow_html=True)


def display_chat_page():
    st.title("Chat with AI")

    logout_url = auth0_app_url + "/logout"
    st.markdown(f'<a href="{logout_url}"><button>Logout</button></a>', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?", max_chars=4096):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = generate_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    main()
