#!/data/data/com.termux/files/usr/bin/python

import os
import sys
from time import sleep
from core.rsfcore import *

print("Are you sure want to install routersploit? ( y or n )")
permission = input(">>> ")

if permission == 'y':
	print("Now installing routersploit...")
	sleep(2)
	runscript()

elif permission == 'n':
	print("Aborting download...")

else:
	print("Dont know lang... Exiting...")
