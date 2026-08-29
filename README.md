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
- **대량생산 카드뉴스 팩토리** — 40~60대 공감 정보성 카드뉴스를 원클릭으로 일괄 생성
  - 공신력(통계청·한국은행·KB·국민연금공단 등) 데이터만 사용, AI가 수치를 지어내지 않음
  - **S/A/B/C 티어리스트** 형식 · 카드 1장 = 세로(9:16) 1080×1920 **4초 리빌(줄 순차 등장)** MP4
  - **한글 깨짐 최종 검증(QC)** + 탈락분만 재생성 버튼
  - PNG/MP4 개별·ZIP 일괄 다운로드 + 금요일(17:20)·화요일(17:20) 자동 업로드 일정표(CSV)

## 실행 방법

로컬에서 바로 실행하려면:

```bash
python gui.py
```

제어판(창)이 뜨고 브라우저로 스튜디오가 자동으로 열립니다.
서버만 띄우려면 `python server.py` → http://localhost:8501 접속.

## 데스크톱 프로그램(EXE)으로 만들기

Python 없이 실행되는 단일 파일 `MogiEgg.exe`를 만들 수 있습니다. (Windows)

1. `build_exe.bat` 더블클릭
2. 자동으로 PyInstaller 설치 → 빌드 진행
3. `dist\MogiEgg.exe` 완성 → 더블클릭하면 스튜디오 실행

수동 빌드는:

```bash
pip install pyinstaller
pyinstaller --clean --noconfirm mogieg.spec
```

> `gui.py` = 데스크톱 제어판 런처 · `server.py` = 정적 서버(표준 라이브러리만 사용)
> API 키는 별도 서버 없이 브라우저(localStorage)에 저장되어 각 LLM 공식 API로 직접 전송됩니다.
> GitHub Pages 등 정적 호스팅에도 그대로 배포할 수 있습니다.
> 대량생산 MP4 인코딩은 브라우저 WebCodecs(H.264)를 사용하므로 Chrome/Edge 권장.

## 배포

`main` 브랜치에 푸시하면 GitHub Actions(`.github/workflows/gh-pages.yml`)가 자동으로 GitHub Pages에 배포합니다.
