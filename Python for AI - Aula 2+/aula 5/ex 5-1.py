import tkinter as tk
import pyautogui
from time import sleep

def criar_janela():
   root=tk.Tk()
   root.title("browser")
   root.mainloop()

def pesquisa_google():
    pyautogui.press('Win')
    sleep(1)
    pyautogui.write("Chrome")
    sleep(1)
    pyautogui.press('Enter')
    sleep(1.5)
    for i in range(0, 32):
        pyautogui.press('Tab')
        sleep(0.1)
    pyautogui.press('Enter')
    sleep(1)
    pyautogui.write("test")
    sleep(0.3)
    pyautogui.press('Enter')
    sleep(5)



def pesquisa_youtube():
	pyautogui.press('Win')
	sleep(1)
	pyautogui.write("Youtube")
	sleep(1)
	pyautogui.press('Enter')
	sleep(10)
	for i in range(0,4):
		pyautogui.press('Tab')
		sleep(0.1)
	pyautogui.write("test")
	sleep(0.3)
	pyautogui.press('Enter')

def pesquisa_amazon():
	pyautogui.press('Win')
	sleep(1)
	pyautogui.write("Amazon")
	sleep(1)
	pyautogui.press('Enter')
	sleep(3)
	pyautogui.press('Tab')
	sleep(0.5)
	pyautogui.press('Enter')
	sleep(2)
	pyautogui.click(803,142)
	sleep(0.5)
	pyautogui.write("test")
	pyautogui.press('Enter')

pesquisa_google()
pesquisa_youtube()
pesquisa_amazon()