#!/bin/bash

while : 
do
	if [ $(date +%H:%M) = "$1" ]; then
		break;
	fi
done

echo "Reiniciando . . ."
sleep 3;
reboot

