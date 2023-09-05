#!/bin/bash

cd /mnt/d/DevOps_HerVired/CICD/CICD_Project/
sudo service nginx stop
sudo cp -rf *.html /var/www/html/
sudo service nginx restart

#some more thing as per requirements like lsof , port checking wil be added n future
