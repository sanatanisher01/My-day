@echo off
REM Batch script to run the MyDay application on Windows

echo MyDay Server Launcher
echo =====================

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH. Please install Python 3.8 or higher.
    exit /b 1
)

REM Check if virtual environment exists, create if not
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements if needed
if not exist venv\Scripts\gunicorn.exe (
    echo Installing requirements...
    pip install -r requirements.txt
)

REM Parse command line arguments
set MODE=prod
set PORT=8000
set WORKERS=3

:parse_args
if "%~1"=="" goto run_server
if "%~1"=="--mode" (
    set MODE=%~2
    shift
    shift
    goto parse_args
)
if "%~1"=="--port" (
    set PORT=%~2
    shift
    shift
    goto parse_args
)
if "%~1"=="--workers" (
    set WORKERS=%~2
    shift
    shift
    goto parse_args
)
shift
goto parse_args

:run_server
REM Run the server
echo Running server in %MODE% mode on port %PORT%...
python run_server.py --mode=%MODE% --port=%PORT% --workers=%WORKERS%

pause
