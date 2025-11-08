import pyautogui
from time import sleep
import os

def criar():
    pyautogui.hotkey('Win','s')
    pyautogui.write("Bloco")
    sleep(0.1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write("Nome:\nEmail:\nMorada:\nPostal:\n")

def guardar():
    pyautogui.hotkey('Ctrl','s')
    sleep(0.5)
    pyautogui.write("Formulario")
    sleep(0.5)
    pyautogui.press('enter')

criar()
guardar()
