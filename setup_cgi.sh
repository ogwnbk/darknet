#!/bin/bash

if [ ! -e "yolov3.weights" ]; then
	wget https://pjreddie.com/media/files/yolov3.weights
fi

sudo chmod 777 /usr/lib/cgi-bin/
sudo chmod 777 /var/www/html/
mkfifo /usr/lib/cgi-bin/darknet_in
mkfifo /usr/lib/cgi-bin/darknet_out
chmod 666 /usr/lib/cgi-bin/darknet_in
chmod 666 /usr/lib/cgi-bin/darknet_out

chmod 755 darknet.cgi
cp darknet.cgi /usr/lib/cgi-bin/

sudo apt install apache2
sudo a2enmod cgid
sudo apt install libcgi-pm-perl
sudo service apache2 start

#チューニングするならthreshオプションで。
#sudo ./darknet detect cfg/yolov3.cfg yolov3.weights -thresh .1
sudo ./darknet detect cfg/yolov3.cfg yolov3.weights
