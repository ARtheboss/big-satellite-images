import pyautogui
import time
import sys
from PIL import Image


x_overlap_adjust = 110
y_overlap_adjust = 70

pause_len = 0.1

drag_dur = 1



def moveLeft():
	pyautogui.moveTo(100, 300, duration=0)
	pyautogui.dragTo(1200, 300, drag_dur, pyautogui.easeOutQuad)

def moveRight():
	pyautogui.moveTo(1200, 300, duration=0)
	pyautogui.dragTo(100, 300, drag_dur, pyautogui.easeOutQuad)

def moveDown():
	pyautogui.moveTo(600, 850, duration=0)
	pyautogui.dragTo(600, 150, drag_dur, pyautogui.easeOutQuad)

def moveUp():
	pyautogui.moveTo(600, 150, duration=0)
	pyautogui.dragTo(600, 800, drag_dur, pyautogui.easeOutQuad)

pyautogui.click(x=500, y=500)

'''
TERMINAL: python /Users/home/Desktop/racetrackscreenshot.py

PRESET URL: https://www.google.com/maps/@1.2969769,103.8494468,235m/data=!3m1!1e3
'''

answer = ""


width_frames = 0

while answer != "stop":
	pyautogui.click(x=500, y=500)
	width_frames += 1
	moveRight()
	pyautogui.click(x=1400, y=500)
	answer = input("Type stop if at required width")
pyautogui.click(x=500, y=500)
for i in range(width_frames):
	moveLeft()

width_frames += 1

width = 1100



answer = ""


height_frames = 0

while answer != "stop":
	pyautogui.click(x=500, y=500)
	height_frames += 1
	moveDown()
	pyautogui.click(x=1400, y=500)
	answer = input("Type stop if at required height")
pyautogui.click(x=500, y=500)
for i in range(height_frames):
	moveUp()

height_frames += 1

height = 700



images = []

for i in range(height_frames):
	images.append([])
	for j in range(width_frames):
		time.sleep(pause_len)
		im1 = pyautogui.screenshot(region=(100,150, width, height))
		if i % 2 == 0:
			print(f"Captured: {i}-{j}.png")
			images[i].append(im1)
		else:
			print(f"Captured: {i}-{(width_frames-1)-j}.png")
			images[i] = [im1] + images[i]
		if j != (width_frames - 1):
			if i % 2 == 0:
				moveRight()
			else:
				moveLeft()
	moveDown()

total_width = width_frames * (width - x_overlap_adjust)
total_height = height_frames * (height - y_overlap_adjust)

new_images = []
for a in range(len(images)):
	new_images.append(Image.new('RGB', (total_width, height)))

for i in range(height_frames):
	x_off = 0
	for j in range(width_frames):
		new_images[i].paste(images[i][j],(x_off,0))
		x_off += width - x_overlap_adjust

final = Image.new('RGB', (total_width, total_height))

y_off = 0
for a in new_images:
	final.paste(a,(0,y_off))
	y_off += height - y_overlap_adjust

final.save('final.png')


