#!/usr/bin/bash
#
# masscan -p80 188.117.30.83
# Discovered open port 80/tcp on 188.117.30.83
#
# masscan -p80 188.117.0.0/18
# Discovered open port 80/tcp on 188.117.31.150
# Discovered open port 80/tcp on 188.117.13.136
# Discovered open port 80/tcp on 188.117.31.150
# Discovered open port 80/tcp on 188.117.13.136
# Discovered open port 80/tcp on 188.117.30.185
# Discovered open port 80/tcp on 188.117.16.99
# Discovered open port 80/tcp on 188.117.46.101
# Discovered open port 80/tcp on 188.117.25.42


while read -r IP_RANGE
do

    masscan -p80 $IP_RANGE

done < "fi.zone"
