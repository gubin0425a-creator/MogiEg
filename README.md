---
title: MogiEgg
emoji: 🥚
colorFrom: emerald
colorTo: cyan
sdk: static
pinned: false
license: mit
---

# 모기에그 (MogiEgg) 🥚

우리만의 AI 숏폼 & 마케팅 스튜디오.
콘텐츠 기획부터 유튜브 분석, 3초 훅 숏폼 제작까지 한 곳에서.

## 주요 기능

- **AI 마케팅 채팅** — Gemini / OpenAI / Claude / Ollama 등 원하는 LLM을 연결해 마케팅 아이디어를 대화로
- **유튜브 & SNS 분석** — 채널·영상 딥다이브 분석, 알고리즘 노출 지수와 잠재 고객 분석
- **3초 훅 숏폼 팩토리** — 주제만 입력하면 훅, 씬별 타임라인, BGM 가이드까지 대본 자동 생성
- **80+ AI 스킬 라이브러리** — 최적화된 프롬프트 프리셋을 원클릭으로

## 실행 방법

로컬에서 바로 실행하려면:

```bash
python server.py
```

브라우저에서 http://localhost:8501 접속.

Windows에서는 `run_studio.bat`을 더블클릭하면 서버가 뜨고 브라우저가 자동으로 열립니다.

> API 키는 별도 서버 없이 브라우저(localStorage)에 저장되어 각 LLM 공식 API로 직접 전송됩니다.
> GitHub Pages 등 정적 호스팅에도 그대로 배포할 수 있습니다.

## 배포

`main` 브랜치에 푸시하면 GitHub Actions(`.github/workflows/gh-pages.yml`)가 자동으로 GitHub Pages에 배포합니다.
