apt-get update
apt-get install -y wget build-essential libncursesw5-dev libreadline-gplv2-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev libbz2-dev libffi-dev \
libz-dev libncursesw5-dev libssl-dev libgdbm-dev libsqlite3-dev libbz2-dev liblzma-dev tk-dev libdb-dev

rm -rf /var/lib/apt/lists/*

wget https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tar.xz
tar -xf Python-3.6.10.tar.xz

cd Python-3.6.10
./configure
make
make install

python3.6 -m venv venv
source venv/bin/activate