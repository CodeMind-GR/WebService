import streamlit as st
import boto3  # AWS SDK를 임포트합니다.
from datetime import datetime
from zoneinfo import ZoneInfo

# Streamlit 페이지 설정
st.set_page_config(page_title="CodeMind Project", layout="wide")

# DynamoDB에 연결합니다.
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('User')

token = st.query_params.get_all("token")
email = st.query_params.get_all("email")
name = st.query_params.get_all("name")

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

    # 로그인 버튼이 클릭되면 외부 인증 서버로 리디렉션하는 자바스크립트를 포함하는 HTML 버튼
    auth_url = "http://localhost:3000/login"  # 외부 인증 서버의 URL
    st.markdown(f'<a href="{auth_url}"><button>Login to Chat</button></a>', unsafe_allow_html=True)


def display_chat_page():
    st.title("Chat with AI")

    # 자동 리디렉션을 위한 로그아웃 링크
    logout_url = "http://localhost:3000/logout"  # 여기서는 예시로 localhost를 사용했습니다. 실제 URL로 교체해야 합니다.
    streamlit_app_url = "http://localhost:8501"  # Streamlit 앱의 홈 URL. 실제 환경에 맞게 수정해야 합니다.

    # 로그아웃 버튼 대신 사용할 자바스크립트를 포함하는 링크
    st.markdown(f'<a href="{logout_url}"><button>Logout</button></a>', unsafe_allow_html=True)

    # 컨테이너 및 레이아웃 구성
    input_container = st.container()
    chat_container = st.container()

    # 채팅 입력 필드
    with input_container:
        user_input = st.text_input("Type your message here:")

    # 채팅 출력 영역
    with chat_container:
        if user_input:
            # 여기에 모델을 호출하는 코드를 추가하고 결과를 변수에 할당하세요.
            model_response = f"You said: '{user_input}'"  # 예시 응답

            # 사용자의 질문과 모델의 응답을 번갈아 표시
            st.text_area("Chat", value=f"You: {user_input}\nAI: {model_response}", height=300, disabled=True)

if __name__ == '__main__':
    main()