#!/bin/sh
 
ip_target=$(cat ~/.config/polybar/bin/.target.tmp | awk '{print $1}')
name_target=$(cat ~/.config/polybar/bin/.target.tmp | awk '{print $2}')

    if [ $ip_target ] && [ $name_target ]; then
        echo "%{F#a8326b}󰩷 %{u-}%{F#ffffff}$ip_target - $name_target"
    elif [ $(cat ~/.config/polybar/bin/.target.tmp | wc -w) -eq 1 ]; then
        echo "%{F#a8326b}󰩷 %{u-}%{F#ffffff} $ip_target "
    else
        echo "%{F#a8326b}󰩷 %{u-}%{F#ffffff} No target"
    fi
