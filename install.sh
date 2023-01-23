#!/bin/bash

git clone https://github.com/iruka-crow/Password-Manager
sudo mv ./Password-Manager /etc/Password-Manager
cd /etc/Password-Manager/src/Linux
sudo mv ./pass-manager /usr/local/bin/pass-manager
sudo mv ./passmg-uninstall /usr/local/bin/passmg-uninstall

sudo chmod 755 /usr/local/bin/pass-manager
sudo chmod 755 /usr/local/bin/passmg-uninstall

echo "Password-Manager Installed."
