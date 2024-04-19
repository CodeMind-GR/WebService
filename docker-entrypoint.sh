#!/bin/bash
# 필요한 환경 변수가 설정되었는지 확인
if [ -z "$AUTH0_APP_URL" ]; then
    echo "AUTH0_APP_URL is not set. Defaulting to 'http://localhost:3000'."
    export AUTH0_APP_URL='http://localhost:3000'
fi

# 필요한 서비스가 실행될 때까지 대기
echo "Waiting for dependent services to be up..."
sleep 10  # 예시로 10초 대기

# Streamlit 앱 실행
exec streamlit run app.py "$@"
