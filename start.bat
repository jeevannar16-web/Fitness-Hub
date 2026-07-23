@echo off
REM Fitness Hub - One-Click Startup Script
REM Works on Windows (CMD, PowerShell, Git Bash)

echo.
echo   ╔═══════════════════════════════════════╗
echo   ║        Fitness Hub - Starting         ║
echo   ╚═══════════════════════════════════════╝
echo.

REM ── Navigate to script directory ──
cd /d "%~dp0"

REM ── Check Python ──
where python >nul 2>nul
if %errorlevel% neq 0 (
    where python3 >nul 2>nul
    if %errorlevel% neq 0 (
        echo   [ERROR] Python is not installed.
        echo   Install it from: https://www.python.org/downloads/
        pause
        exit /b 1
    )
    set PYTHON=python3
) else (
    set PYTHON=python
)

for /f "tokens=*" %%i in ('%PYTHON% --version 2^>^&1') do echo   Using %%i

REM ── Create virtual environment ──
if not exist "venv" (
    echo   [1/5] Creating virtual environment...
    %PYTHON% -m venv venv
) else (
    echo   [1/5] Virtual environment found.
)

REM ── Activate ──
echo   [2/5] Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo   [ERROR] Could not find venv activation script.
    pause
    exit /b 1
)

REM ── Upgrade pip silently ──
python -m pip install --upgrade pip -q 2>nul

REM ── Install dependencies ──
echo   [3/5] Installing dependencies...
pip install -r requirements.txt -q

REM ── Run migrations ──
echo   [4/5] Setting up database...
python manage.py migrate

REM ── Seed sample data ──
echo   [5/5] Loading sample data...
python seed_data.py

echo.
echo   ╔═══════════════════════════════════════════════╗
echo   ║  Fitness Hub is running!                      ║
echo   ║                                               ║
echo   ║  Open in browser:  http://localhost:8000       ║
echo   ║  Admin panel:      http://localhost:8000/admin ║
echo   ║                                               ║
echo   ║  Press Ctrl+C to stop the server              ║
echo   ╚═══════════════════════════════════════════════╝
echo.

python manage.py runserver 0.0.0.0:8000

pause
