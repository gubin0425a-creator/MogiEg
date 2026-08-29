# MogiEgg — 가벼운 정적 스튜디오 서버
FROM python:3.12-slim

WORKDIR /app

# 의존성 없이 표준 라이브러리만 사용
COPY . /app/

# MogiEgg 스튜디오 포트
EXPOSE 8501

CMD ["python", "server.py"]
