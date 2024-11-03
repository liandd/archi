#!/bin/bash

#echo "%{F#ffffff}$(/usr/bin/ifconfig wlp2s0 | grep "inet" | awk '{print $2}')%{u-}"
echo "%{F#ffffff}$(/usr/bin/ifconfig wlp3s0 | grep "inet" | awk '{print $2}')%{u-}"
