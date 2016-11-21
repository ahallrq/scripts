#!/bin/bash

url="http://www.google.com.au/"

function geturl()
{
  dialog --title "Url" --inputbox "Type a url to visit or leave blank..." 0 80 2> /tmp/.shelllogin-links-url$$
  if [ $? -eq 0 ]
  then
    url=$(</tmp/.shelllogin-links-url$$)
    rm /tmp/.shelllogin-links-url$$
  fi
}

dialog --title "Browser" --menu "Choose a browser to start..." 12 50 12 \
       links "Links browser" \
       glinks "Links browser (graphical)" \
       elinks "ELinks browser" \
       -------- "---------------" \
       lynx "Lynx browser" \
       2> /tmp/.shelllogin-links$$

if [ $? -eq 0 ]
then
  option=$(</tmp/.shelllogin-links$$)
  rm /tmp/.shelllogin-links$$
  clear
  case $option in
    links	)  geturl; links $url;;
    glinks	)  geturl; links -g $url;;
    elinks	)  geturl; elinks $url;;
    lynx	)  geturl; lynx $url;;
  esac
  exit 0
else
  exit 1
fi
