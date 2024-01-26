#!/bin/bash

HISTFILE=~/bash.history
set -o history

echo "Hola putas"
cd /
cd ~
pwd
ls
sleep 2
touch test.txt
cp test.txt test2.txt
mv test2.txt test3.txt
mkdir prueba
mv test3.txt prueba
cp -r prueba prueba2
rm -r prueba
mv test.txt prueba2
cd prueba2
echo "Hola" >> test3.txt
echo "Mundo" >> test4.txt
cat test3.txt test4.txt > test5.txt
clear
whoami
sleep 2
cat test3.txt
sleep 2
netstat --help
sleep 5
clear
history

