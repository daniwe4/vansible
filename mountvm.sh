#!/bin/bash

ip=$(vagrant ssh $1 -c "ip address show eth1" 2>/dev/null | sed -ne '/inet / s/\s\+inet \([^\/]\+\).*\r/\1/p')
dir=$HOME/mount/$1

mkdir -p $HOME/mount
mkdir -p $dir


sshfs root@$ip:/home/vagrant $dir