import os
import sys
import time

import pyautogui

# รูปปุ่มต้องอยู่โฟลเดอร์เดียวกับ exe (หรือ .py)
BASE = os.path.dirname(sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__))
BTN1 = os.path.join(BASE, "btn1.png")
BTN2 = os.path.join(BASE, "btn2.png")

CONFIDENCE = 0.85   # ความเหมือนของรูป 0-1 (ต่ำ = จับง่ายแต่พลาดได้)
POLL = 0.3          # เช็กหน้าจอทุกกี่วินาที
AFTER_CLICK = 0.2   # หน่วงสั้นๆ หลังคลิก

pyautogui.FAILSAFE = True  # ลากเมาส์ไปมุมซ้ายบนของจอเพื่อหยุดโปรแกรม


def find(path):
    try:
        return pyautogui.locateCenterOnScreen(path, confidence=CONFIDENCE)
    except pyautogui.ImageNotFoundException:
        return None


def wait_and_click(path, name):
    """รอจนปุ่มโผล่มา แล้วคลิก"""
    while True:
        pos = find(path)
        if pos:
            pyautogui.click(pos)
            print(f"คลิก {name} ที่ {pos.x},{pos.y}")
            time.sleep(AFTER_CLICK)
            return
        time.sleep(POLL)


def main():
    for p in (BTN1, BTN2):
        if not os.path.exists(p):
            input(f"ไม่พบไฟล์ {p}\nกด Enter เพื่อปิด")
            return
    print("เริ่มทำงาน (ลากเมาส์ไปมุมซ้ายบนของจอ หรือกด Ctrl+C เพื่อหยุด)")
    time.sleep(2)
    n = 0
    while True:
        time.sleep(3)
        wait_and_click(BTN1, "ปุ่ม 1")   # รอปุ่ม 1 โผล่ -> คลิก
        time.sleep(3)
        wait_and_click(BTN2, "ปุ่ม 2")   # รอปุ่ม 2 โผล่ -> คลิก
        n += 1
        print(f"--- รอบที่ {n} ---")


if __name__ == "__main__":
    try:
        main()
    except pyautogui.FailSafeException:
        print("หยุดโดย failsafe")
    except KeyboardInterrupt:
        print("หยุดแล้ว")
