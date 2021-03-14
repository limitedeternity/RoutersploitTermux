cd $HOME

echo "[*] Installing requirements..."
apt update && apt upgrade -y
pkg upgrade && pkg install autoconf automake bison bzip2 clang cmake coreutils diffutils flex gawk git grep gzip libtool make patch perl sed silversearcher-ag tar wget pkg-config -y
pkg install python rust libcrypt libffi openssl -y

echo "[*] Cloning routersploit..."
git clone https://github.com/threat9/routersploit
cd routersploit

echo "[*] Installing requirements with python3-pip..."
python3 -m pip install --upgrade pip
python3 -m pip install wheel future
python3 -m pip install -r requirements.txt

echo "[*] All done!"
cd $HOME
echo "Run: cd routersploit && python3 rsf.py"
