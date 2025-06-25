@echo off
echo Starting Backend...
start cmd /k "cd /d C:\blackcoffer-dashboard\backend && python -m uvicorn main:app --reload"

timeout /t 2 > nul

echo Starting Frontend...
start cmd /k "cd /d C:\blackcoffer-dashboard\frontend && npm start"
