import pyautogui
import time

def cautare_google():
    if pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\camp_google.png', confidence=0.7) is not None:
        camp_google = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\camp_google.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://www.emag.ro/")
        pyautogui.press('enter')
        time.sleep(2)

        pc_periferice_software = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\pc_periferice_software.png', confidence=0.7)
        pyautogui.click(pc_periferice_software)
        time.sleep(1)

        desktop_pc = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\desktop_pc.png', confidence=0.7)
        pyautogui.click(desktop_pc)
        time.sleep(2)

        show_notepad = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\notepad.png', confidence=0.7)

        minimize_notepad = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\minimize.png', confidence=0.7)

        back = pyautogui.locateOnScreen(r'D:\Inteligenta Artificiala\PROIECT COLOCVIU\proiect\back.png', confidence=0.7)

        camp_url = 407, 78
        copy_url = 479, 296
        page_notepad = 1600, 910
        paste = 1665, 527

        x = 741
        y = 938

        for j in range(0, 3):
            for i in range(0, 4):
                time.sleep(2)
                pyautogui.click(pyautogui.position(x, y))
                time.sleep(2)
                pyautogui.click(camp_url)
                time.sleep(1)
                pyautogui.rightClick()
                time.sleep(1)
                pyautogui.click(copy_url)
                time.sleep(1)
                pyautogui.click(show_notepad)
                time.sleep(1)
                pyautogui.click(page_notepad)
                time.sleep(1)
                pyautogui.rightClick()
                time.sleep(1)
                pyautogui.click(paste)
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(minimize_notepad)
                time.sleep(1)
                pyautogui.click(back)
                time.sleep(2)
                x = x + 362
                pyautogui.scroll(392)
            time.sleep(2)
            x = 741
            pyautogui.moveTo(x, y)
            pyautogui.scroll(-550)

    else:
        print("IMAGINEA NU SE AFLA PE ECRAN")


def coordonate():
    print(pyautogui.position())

time.sleep(1.5)
coordonate()
cautare_google()