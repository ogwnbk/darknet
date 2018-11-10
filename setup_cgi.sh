#!/bin/bash

if [ ! -e "yolov3.weights" ]; then
	wget https://pjreddie.com/media/files/yolov3.weights
fi

sudo chmod 777 /usr/lib/cgi-bin/
mkfifo /usr/lib/cgi-bin/darknet_in
mkfifo /usr/lib/cgi-bin/darknet_out

sudo apt install apache2
sudo service apache2 start

make
sudo ./darknet detect cfg/yolov3.cfg yolov3.weights
