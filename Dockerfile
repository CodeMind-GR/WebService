# 베이스 이미지를 Python 3.9로 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 앱 파일 복사
COPY . /app

# docker-entrypoint.sh 추가
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# 포트 8501 열기
EXPOSE 8501

# 엔트리포인트 설정
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
# Streamlit 앱 실행
# CMD ["streamlit", "run", "app.py"]
