#########################################################################
# File Name: autoInit.sh
# Author: pchwu
# Created Time: 2017年06月07日 星期三 16时49分03秒
#########################################################################
#!/bin/bash

# 设置vim的属性  start
sudo apt-get install exuberant-ctags
cp ./vimrc ~/.vim/vimrc
cp ./vimplugin.gz ~/.vim
cd ~/.vim 
tar -zxvf ./vimplugin.gz
cd -
#end

#git配置快捷命令
cp ./.gitconfig ~/.gitconfig
