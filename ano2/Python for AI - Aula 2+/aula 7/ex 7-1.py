import pyautogui
import tkinter as tk
import os
from tkinter import messagebox
from time import sleep


def gui():
    root = tk.Tk()
    root.geometry("200x200")
    root.wm_resizable(False, False)

    label = tk.Label(root,text="Nome da imagem:")
    label.place(x=15, y=10)

    entry = tk.Entry(root, width=25)
    entry.place(x=20, y=35)

    button = tk.Button(root, text="Capturar", command=lambda: screenshot(entry.get()), height=5, width=20)
    button.place(x=20, y=90)

    root.mainloop()


def screenshot(nomef):
    if os.path.exists(fr"C:\Users\shark\PycharmProjects\ano2\Python for AI - Aula 2+\aula 7\screenshots\{nomef}.png"):
        while os.path.exists(fr"C:\Users\shark\PycharmProjects\ano2\Python for AI - Aula 2+\aula 7\screenshots\{nomef}.png"):
            nomef = nomef + "_C"

    im = pyautogui.screenshot()

    try:
        im.save(fr"C:\Users\shark\PycharmProjects\ano2\Python for AI - Aula 2+\aula 7\screenshots\{nomef}.png")
        sleep(1)
        messagebox.showinfo("Print Screen","Guardando imagem...")
    except ValueError:
        messagebox.showerror("Print Screen","Pôe um Nome na caixa!")

gui()
