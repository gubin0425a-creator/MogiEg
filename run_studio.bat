@echo off
title MogiEgg Studio
cd /d "%~dp0"
echo Starting MogiEgg Studio...
start "" http://localhost:8501
python server.py
pause
