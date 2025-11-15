import pyautogui
from tkinter import messagebox
from time import sleep

messagebox.showinfo('AimBot', 'Ok para Iniciar')

while True:

    x,y=pyautogui.position()

    r,g,b=pyautogui.pixel(x,y)

    if r==75 and g==219 and b==106:
       pyautogui.click(x, y)
       sleep(1)
       break

