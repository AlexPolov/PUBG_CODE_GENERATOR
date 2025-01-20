@echo off
:: Check if Python is installed
where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed on this system.
    echo Please install Python from https://www.python.org/.
    pause
    exit
)

:: Run setup.py if config.json doesn't exist
if not exist config.json (
    echo Running setup to create config.json...
    python setup.py
)

:: Run the main program
echo Starting CodeManipulator...
python CodeManipulator.py
pause
