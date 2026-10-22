@echo off
pip install pyautogui opencv-python pillow pyinstaller
pyinstaller --onefile --name auto_click auto_click.py
echo.
echo เสร็จแล้ว: dist\auto_click.exe  (วาง btn1.png และ btn2.png ไว้ข้างๆ)
pause
