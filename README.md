# Password-Manager

##インストール方法

## ディレクトリ構成 
Password-Manager  
│  
├ /src  
│  ├ main.py  
│  │  * メイン Python プログラム  
│  │  * /etc/Password-Manager/passc 内にシステムファイルをつくります。（Linuxの場合）システム的にはmain.pyと同じディレクトリにつくります。  
│  ├ / Linux  
│  │  ├ / pass-manager  
│  │  │    * Linux用プログラム起動スクリプト  
│  │  └ / passmg-uninstall  
│  │       * Linux用プログラムのアンインストール用スクリプト  
│  │  
│  └ / Windows  
│     │  
│     ├ / pass-manager  
│     │    * Windows用プログラム起動バッチファイル  
│     └ / passmg-uninstall  
│          * Windows用プログラムのアンインストール用バッチファイル  
├ / install.sh  
│    * Linux用インストールshファイル  
└ / install.bat  
     * Windows用インストールバッチファイル   
     
> English

## How to Install

## Directory Tree  
Password-Manager  
│  
├ /src  
│  ├ main.py  
│  │  * Main python program  
│  │  * Make system file in /etc/Password-Manager/passc on Linux. (make folder on [main.py]'s directory)  
│  ├ / Linux  
│  │  ├ / pass-manager  
│  │  │    * Program start script for Linux  
│  │  └ / passmg-uninstall  
│  │       * Program set file uninstaller for Linux  
│  │  
│  └ / Windows  
│     │  
│     ├ / pass-manager  
│     │    * Program start script for Linux  
│     └ / passmg-uninstall  
│          * Program set file uninstaller for Linux  
├ / install.sh  
│    * Install this branch's file on Linux  
└ / install.bat  
     * Install this branch's file on Windows   
