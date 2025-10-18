import pyautogui
from time import sleep

# Open paint
pyautogui.press('win')
pyautogui.write("paint")
sleep(1)
pyautogui.press('enter')

# Select circle
sleep(1)
pyautogui.moveTo(562,81,1)
pyautogui.click()
pyautogui.moveTo(800,500,1)
pyautogui.dragTo(1600,800,1)

# Select bucket
sleep(1)
pyautogui.moveTo(370,80,1)
pyautogui.click()
pyautogui.moveTo(1123,82,1)
pyautogui.click()
pyautogui.moveTo(1300,600,1)
pyautogui.click()


