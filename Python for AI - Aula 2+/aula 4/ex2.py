import pyautogui
from time import sleep

nome=str(input("Nome: "))
email=str(input("Email: "))
morada=str(input("Morada: "))
CP=str(input("Codigo Postal: "))

def abrir_formulario():
    pyautogui.hotkey('Win','s')
    sleep(0.1)
    pyautogui.write("Formulario")
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)

    pyautogui.keyDown('Alt')
    sleep(0.5)
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.keyUp('Alt')

def preencher():
    for i in range(0,5):
        pyautogui.press('right')

    pyautogui.write(nome)
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)

    pyautogui.write(email)
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)

    pyautogui.write(morada)
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)

    pyautogui.write(CP)
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)

def guardar():
    pyautogui.hotkey('Ctrl','s')
    pyautogui.hotkey('Alt','f4')

abrir_formulario()
preencher()
guardar()