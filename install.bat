@echo off

cd ..
move .\Password-Manager %HOMEPATH%
cd %HOMEPATH%
cd .\Password-Manager\src\Windows
move .\pass-manager C:\Windows\system32
move .\passmg-uninstall C:\Windows\system32

echo "Installed"
exit
