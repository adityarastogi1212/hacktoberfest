# You need pyautogui module for this - pip install pyautogui

import pyautogui
import time

choice = int(input("Do you want to spam\n 1.text\n2.file\n"))


def text():
	text = input("Enter your message here: \n")
	num = int(input("How many times you wanna spam it? \n"))
	entr = input("Press Enter to start")
	time.sleep(4)
	a = 0
	while a<num:
		pyautogui.write(text, interval=0.001)  # type with quarter-second pause in between each key
		pyautogui.press('enter')
		a = a+1


def image_():
	print("Please copy the file you want to send\n")
	num = int(input("How many times you wanna spam it? \n"))
	entr = input("Press Enter to start")
	time.sleep(5)
	a = 0
	while a<num:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('enter')
		a = a+1


if choice==1:
	text()
elif choice==2:
	image_()



