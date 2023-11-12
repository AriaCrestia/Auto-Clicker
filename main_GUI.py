import tkinter as tk
from tkinter import ttk
import pyautogui
from pynput.keyboard import Key, Listener
import threading
import time

pos1 = pyautogui.position()
pos2 = pyautogui.position()

class Button_Ev:    
	def Start_Ev():
		if buttonStart["text"] == "Start(R)":
			buttonStart["text"] = "Stop(R)"
			Mouse_Ev.Clicker()
			buttonStart["text"] = "Start(R)"
		# elif buttonStart["text"] == "Stop(R)":
		# 	buttonStart["text"] = "Start(R)"
	def Exit_Ev():
		window.destroy()

class Mouse_Ev:
	def Clicker():
		pyautogui.click(pos1)
		time.sleep(1)
		pyautogui.click(pos2)
		time.sleep(1)

class Keyboard_Ev:
	def Listen(command=""):
		with Listener(on_press=Keyboard_Ev.UserInput) as ListenStart:
			ListenStart.join()
		if command == "e":
			ListenStart.stop()
	def UserInput(key):
		global pos1, pos2
		try:
			if str(key.char).lower() == "r":
				Button_Ev.Start_Ev()
			elif str(key.char).lower() == "e":
				Button_Ev.Exit_Ev()
			elif str(key.char) == "1":
				pos1 = pyautogui.position()
				point1["text"] = pos1
			elif str(key.char) == "2":
				pos2 = pyautogui.position()
				point2["text"] = pos2
			else:
				pass
		except Exception as e:
			pass

listenThread = threading.Thread(target=Keyboard_Ev.Listen)
listenThread.start()

window = tk.Tk()
window.title("Auto Clicker - Shiro")

pointFrameText = tk.Frame(master=window)
point1Text = tk.Label(master=pointFrameText, text="Point 1", font=["Monospace", 20])
point2Text = tk.Label(master=pointFrameText, text="Point 2", font=["Monospace", 20])
point1Text.pack(side="left", padx=10)
point2Text.pack(side="right", padx=10)
pointFrameText.pack()

pointFrameNums = tk.Frame(master=window)
point1 = tk.Label(master=pointFrameNums, text="0", font=["Monospace", 20])
point2 = tk.Label(master=pointFrameNums, text="0", font=["Monospace", 20])
point1.pack(side="left", padx=50)
point2.pack(side="right", padx=50)
pointFrameNums.pack()

status = tk.Label(master=window, text="")
status.pack(pady=10)
buttonStart = ttk.Button(master=window, text="Start(R)", command=Button_Ev.Start_Ev)
buttonStart.pack(side="left", padx=15, pady=10)
buttonExit = ttk.Button(master=window, text="Exit", command=Button_Ev.Exit_Ev)
buttonExit.pack(side="right", padx=15, pady=10)

window.mainloop()
# threading.main_thread().join()
exit(0)