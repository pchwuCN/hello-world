#########################################################################
# File Name: install_pip.sh
# Author: pchwu
# Created Time: 2017年06月08日 星期四 21时20分03秒
#########################################################################
#!/bin/bash

wget 'http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz'
tar zxvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
python setup.py build
sudo python setup.py install

cd ..
wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate
tar -xzvf pip-1.5.4.tar.gz
cd pip-1.5.4
sudo python setup.py install
#rm pip-1.5.4.tar.gz
