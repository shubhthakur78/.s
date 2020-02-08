

import pyautogui
import time
from PIL import ImageGrab,ImageOps
from numpy import *

class Coordinate():
	replayButton = (684, 356)
	dinosaur = (425, 398)
	# x = 490
	# y = 400

'''	
	This function is used to res   tart the game
'''
def restart_game():
	pyautogui.click(Coordinate.replayButton)
	
'''	
	This function is used to perform jumping of dinosaur
'''
def press_space():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("Jump")
	pyautogui.keyUp('space')
	
def image_grab():
	# Coordinates of box where we want the dinosaur should jump to avoid collision
	box = (Coordinate.dinosaur[0]+60, Coordinate.dinosaur[1], Coordinate.dinosaur[0]+100, Coordinate.dinosaur[1]+30)
	# pass the coordinates of box in grab() function to grab the area of box( i.e. pixels of box in RGB).
	image = ImageGrab.grab(box)
	# convert the grabbed image in grayscale(i.e. RGB pixels into grascale pixels)
	gray_image = ImageOps.grayscale(image)
	# extract the grayscale pixel's value in an array 
	a = array(gray_image.getcolors())
	# return the sum of all the pixels inside the box.
	return a.sum()       
	print(a.sum())

#
# restart_game()
# while True:
# 	image_grab()


def main():
	restart_game()
	while True:
		# if sum of all the pixels is 1447 it means their is no obstacle (free space to run)
		# if sum of all the pixels is not eq     ual to 1447 that means their is an obstacle(tree or bird)
		if image_grab() != 1530:
			press_space()
			time.sleep(0.1)
main()

