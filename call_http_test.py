#!/usr/bin/bash

NEXT_IP="151.105.96.3"

while true
do
  NEXT_IP=$(python http_test.py $NEXT_IP | tail -1 | cut -d"/" -f3)
  echo $NEXT_IP
  rm html/$NEXT_IP.html
  sleep 60
done
