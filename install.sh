#!/bin/bash

git clone https://github.com/iruka-crow/Password-Manager
sudo mv ./Password-Manager /etc/Password-Manager
cd /etc/Password-Manager/src/Linux
sudo mv -rfp ./pass-manager /usr/local/bin/pass-manager
sudo mv -rfp ./passmg-uninstall /usr/local/bin/passmg-uninstall

sudo chmod 755 /usr/local/bin/pass-manager
sudo chmod 755 /usr/local/bin/passmg-uninstall

echo "Password-Manager Installed."
