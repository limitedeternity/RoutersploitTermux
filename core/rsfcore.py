#!/data/data/com.termux/files/usr/bin/python

import os
import sys
from time import sleep

def runscript():
 print("[*] Initializing...")
 sleep(2)
 os.system("cd $HOME")
 os.system("termux-setup-storage")
 sleep(1)

 print("[*] Installing routersploit requirements with apt...")
 sleep(2)
 os.system("apt update && apt upgrade -y")
 os.system("pkg upgrade && pkg install autoconf automake bison bzip2 clang cmake coreutils diffutils flex gawk git grep gzip libtool make patch perl sed silversearcher-ag tar wget pkg-config -y")
 os.system("pkg install python-dev clang libcrypt-dev libffi-dev git openssl-dev -y")
 sleep(1)

 print("[*] Cloning routersploit...")
 sleep(2)
 os.system("cd $HOME")
 os.system("git clone https://github.com/threat9/routersploit")
 sleep(1)

 print("[*] Installing requirements using python3-pip...")
 sleep(2)
 os.system("cd $HOME")
 os.system("cd routersploit")
 os.system("pip install --upgrade pip")
 os.system("pip install request")
 os.system("python 3 -m pip install -r requirements.txt")
 os.system("python 3 -m pip install -r requirements-dev.txt")
 os.system("cd $HOME")
 
 sleep(1)
 print("[*] All done!")
 sleep(2)
 print("Please terminate termux and run the program...")
 print("")
