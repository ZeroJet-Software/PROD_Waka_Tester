@REM Run this script with a VENV with all dependencies installed


call pyinstaller ^
    --onefile ^
    --noconfirm ^
    --name "Waka control panel" ^
    --add-data "modules/EmDrive.eds:modules" ^
    --contents-directory "modules" ^
    wakacontrolpanel.py