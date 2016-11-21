#!/bin/bash

dialog --title "Window Manager" --menu "Choose a window manager to start..." 22 50 22 \
       i3 "i3 Window Manager" \
       awesome "AwesomeWM" \
       sway "Sway Window Manager (XWayland)" \
       fluxbox "Fluxbox" \
       qtile "QTile Python WM" \
       bspwm "BSPWM" \
       dwm "DWM" \
       spectrwm "SpectrWM" \
       xmonad "Xmonad" \
       wmii "WMii" \
       icewm "IceWM (no session)" \
       icewm-session "IceWM" \
       wmaker "WindowMaker" \
       wm2 "WM2" \
       herbstluftwm "HerbstluftWM" \
       2> /tmp/.shelllogin-wm$$

if [ $? -eq 0 ]
then
  option=$(</tmp/.shelllogin-wm$$)
  rm /tmp/.shelllogin-wm$$
  clear
  case $option in
    i3             ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc i3 solarised; echo -e "\e[0;39m"; clear;;
    awesome        ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc awesome solarised; echo -e "\e[0;39m"; clear;;
    sway           ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc sway solarised; echo -e "\e[0;39m"; clear;;
    fluxbox        ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc fluxbox solarised; echo -e "\e[0;39m"; clear;;
    qtile          ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc qtile solarised; echo -e "\e[0;39m"; clear;;
    bspwm          ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc bspwm solarised; echo -e "\e[0;39m"; clear;;
    dwm            ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc dwm solarised; echo -e "\e[0;39m"; clear;;
    spectrwm       ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc spectrwm solarised; echo -e "\e[0;39m"; clear;;
    xmonad         ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc xmonad solarised; echo -e "\e[0;39m"; clear;;
    wmii           ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc wmii solarised; echo -e "\e[0;39m"; clear;;
    icewm-session  ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc icewm solarised; echo -e "\e[0;39m"; clear;;
    icewm          ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc icewmns solarised; echo -e "\e[0;39m"; clear;;
    wmaker         ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc wmaker solarised; echo -e "\e[0;39m"; clear;;
    wm2            ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc wm2 solarised; echo -e "\e[0;39m"; clear;;
    herbstluftwm   ) clear; echo -e "\e[8;30m"; startx ~/.xinitrc herbstluftwm solarised; echo -e "\e[0;39m"; clear;;
  esac
  exit 0
else
  exit 1
fi
