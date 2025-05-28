import time
import subprocess
import pyautogui
import pyperclip

def send_message(link, index):

    if (index % 2 != 0):
        subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        #subprocess.Popen(r"C:\Users\joao.david\AppData\Local\Programs\Opera GX\opera.exe")
    else: 
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        
    time.sleep(5) 

    pyautogui.hotkey('ctrl', 't')
    time.sleep(2) 

    pyperclip.copy(link)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(2)

    if(index <=1 ):
        time.sleep(60)

    pyautogui.press('f11')
    time.sleep(25) 

    pyautogui.moveTo(800, 700, duration=0.1)
    time.sleep(0.05)

    pyautogui.click()

    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)

    pyautogui.press('enter')