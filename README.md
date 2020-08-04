I make the script to install routersploit on termux.
I get the resolve of many problem installing termux in 
https://github.com/threat9/routersploit/issues/531

I just simplified and fix the command so it will take less storage

# Updates

Now this script can run with shell or python

# Before Installation

1. Reset termux first
2. Dont interfere the installation
3. Keep screen on
4. Have a good internet
5. Enough of space 1GB-700mb
6. Patience
7. Look all the progress for tracking error problems

# Installation

Method 1

```
apt update && apt upgrade
apt install git curl
curl -LO https://raw.githubusercontent.com/41Team/RoutersploitTermux/master/run.sh
bash run.sh
```

Method 2

```
apt update && apt upgrade -y
apt install git python
git clone https://github.com/41Team/RoutersploitTermux
cd RoutersploitTermux
python run.py
```

Note : Dont terminate termux when installation! Please terminate after installation is done.

# How to run routersploit

```
1. cd $HOME
2. cd routersploit
3. python rsf.py
```

Thank you to use my script (If occured a error or fail just send a issue) :)
