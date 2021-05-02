from random import randint
import time

try:
	from pynput.keyboard import Controller
except ImportError:
	print('Install pynput usng "pip install pynput"')

"""Time to sleep between two key presses in seconds"""
_break = 5

keys = ['w','a','s','d']
keyboard = Controller()

def press(t=_break):
	key = keys[randint(0,len(keys)-1)]
	time.sleep(t)
	keyboard.press(key)
	time.sleep(1)
	keyboard.release(key)

if __name__ == '__main__':
	print('Anti Afk running....')
	try:
		while True:
			press()
	except KeyboardInterrupt:
		print('Anti Afk Stopped')