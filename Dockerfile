# Python 이미지를 사용합니다. 
FROM python:3.12.2-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# Python 버퍼링을 비활성화합니다.
ENV PYTHONUNBUFFERED True

# requirements.txt 파일을 컨테이너로 복사합니다.
COPY requirements.txt ./requirements.txt

# requirements.txt에 명시된 필요한 패키지들을 설치합니다.
RUN pip install -r requirements.txt

# 현재 디렉토리의 내용을 컨테이너의 작업 디렉토리로 복사합니다.
COPY . .

# Streamlit의 네트워크 설정을 변경합니다.
EXPOSE 8501

# 컨테이너가 실행될 때 스트림릿 애플리케이션을 실행하는 명령어를 설정합니다.
CMD ["streamlit", "run", "app.py", "--server.port=8501"]

