import pyautogui
import time

def limpeza_de_dados():
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('del /s /q %temp%\\*')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.write('cleanmgr /sagerun:1')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.write('exit')
    time.sleep(1)
    pyautogui.press('enter')