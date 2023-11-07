from pynput.keyboard import Key, Listener
import pyautogui
import threading
import time

clicks = False
positions = ["", ""]

def ClickStart():
	while True:
		while clicks == True:
			pyautogui.click(positions[0])
			time.sleep(1)
			pyautogui.click(positions[1])
			time.sleep(1)

doClicks = threading.Thread(target=ClickStart)
doClicks.start()

def ClickToggle(key):
	try:
		global clicks
		if str(key.char) == "r":
			clicks = not clicks
		elif str(key.char) == "1":
			positions.pop(0)
			positions.insert(0, pyautogui.position())
			print(f"Pos 1: {positions[0]}")
		elif str(key.char) == "2":
			positions.pop(1)
			positions.insert(1, pyautogui.position())
			print(f"Pos 2: {positions[1]}")
		else:
			pass
	except AttributeError:
		print("Invalid character.")

with Listener(on_press=ClickToggle) as ListenStart:
	ListenStart.join()