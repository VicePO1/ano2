import pyautogui
from time import sleep

while True:
	a = pyautogui.position()
	print(a)
	sleep(1)