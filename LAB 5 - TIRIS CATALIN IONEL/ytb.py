import pyautogui
import keyboard
import time

def cautare_google():
   if pyautogui.locateOnScreen(r"D:\Inteligenta Artificiala\LAB-uri\LAB 5\poza1.png", confidence=0.7) != None:
    cam_google=pyautogui.locateOnScreen("D:\Inteligenta Artificiala\LAB-uri\LAB 5\poza1.png", confidence=0.7)
    pyautogui.click(cam_google)
    time.sleep(3)
    pyautogui.write("https://youtube.com")
    pyautogui.press("enter")
   else:
      print("IMAGINE NUU SE AFLA PE ECRAN")


def coordonate():
    print(pyautogui.position())

time.sleep(2)

coordonate()