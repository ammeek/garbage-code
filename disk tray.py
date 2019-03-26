import ctypes
import time
import random

while True:
	
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
	time.sleep(random.randint(5,300))