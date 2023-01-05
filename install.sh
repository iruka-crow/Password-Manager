#!/bin/bash

git clone https://github.com/iruka-crow/Password-Manager
sudo mv ./Password-Manager /etc
cd /etc/Password-Manager
sudo mv ./pass-manager /usr/local

sudo chmod 777 /usr/local/pass-manager

echo "Password-Manager Installed."