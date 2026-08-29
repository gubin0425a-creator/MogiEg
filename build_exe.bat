@echo off
title MogiEgg EXE 빌드
cd /d "%~dp0"
echo ============================================
echo   MogiEgg 단일 실행 파일(EXE) 빌더
echo ============================================
echo [1/3] PyInstaller 설치 중...
pip install pyinstaller
if errorlevel 1 (
    echo PyInstaller 설치에 실패했습니다. Python/PIP 를 확인하세요.
    pause
    exit /b 1
)
echo [2/3] EXE 빌드 중...
pyinstaller --clean --noconfirm mogieg.spec
if errorlevel 1 (
    echo 빌드에 실패했습니다.
    pause
    exit /b 1
)
echo [3/3] 완료!
echo.
echo   실행 파일: dist\MogiEgg.exe
echo   (더블클릭하면 브라우저에서 스튜디오가 열립니다)
echo.
pause
