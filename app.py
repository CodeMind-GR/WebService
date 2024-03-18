import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title='chatGPT-like Interface', layout='wide')

def main():
    st.title('Chat with AI')

    # 컨테이너 및 레이아웃 구성
    input_container = st.container()
    chat_container = st.container()

    # 사이드바 설정 (옵션)
    with st.sidebar:
        st.header('About')
        st.write("This is a simple chat interface using Streamlit.")

    # 채팅 입력 필드
    with input_container:
        user_input = st.text_input("Type your message here:")

    # 채팅 출력 영역
    with chat_container:
        if user_input:
            # 여기에 모델을 호출하는 코드를 추가하고 결과를 변수에 할당하세요.
            # 예시 결과 (실제로는 모델을 통해 생성된 결과를 사용해야 합니다.)
            model_response = f"You said: '{user_input}'"
            
            # 사용자의 질문과 모델의 응답을 번갈아 표시합니다.
            st.text_area("Chat", value=f"You: {user_input}\nAI: {model_response}", height=300, disabled=True)

if __name__ == '__main__':
    main()

