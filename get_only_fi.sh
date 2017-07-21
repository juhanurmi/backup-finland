#!/usr/bin/bash

while read -r IP
do

    grep $IP 20170714_short_prefix_filtered_dns.txt

done < "80_results.log"
