#!/bin/bash

dialog --title "Python Environment" --menu "Choose a python environment to start..." 15 50 15 \
       python "Python shell" \
       ipython "Iron Python shell" \
       bpython "BPython shell" \
       -------- "---------------" \
       python2 "Python 2.x shell" \
       ipython2 "Iron Python 2.x shell" \
       bpython2 "BPython 2.x shell" \
       2> /tmp/.shelllogin-python$$

if [ $? -eq 0 ]
then
  option=$(</tmp/.shelllogin-python$$)
  rm /tmp/.shelllogin-python$$
  clear
  case $option in
    python	)  python;;
    ipython	)  ipython;;
    bpython	)  bpython;;
    python2	)  python2;;
    ipython2    )  ipython2;;
    bpython2	)  bpython2;;
  esac
  exit 0
else
  exit 1
fi
