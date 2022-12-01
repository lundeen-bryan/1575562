@echo off
cd .venv
cd Scripts
activate
cd ../..
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

cls
python main.py

set /p tmp = Hit Enter to close...