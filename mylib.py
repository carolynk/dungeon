from time import sleep
import sys

#scrollTxt by xolyon's, via CodingCactus
def scroll_text(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.05)


# Blue="\033[0;34m"
# Cyan="\033[1;36m"
# Purple="\033[0;35m" 
# Green="\033[0;32m"
# Orange ="\033[0;33m"
# Pink = "\033[1;31m"
# DarkBlue = "\033[1;34m"
# White = "\033[1;37m"
# Default = "\033[1;39m"
