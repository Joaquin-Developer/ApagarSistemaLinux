#!/bin/bash

echo "El sistema se reiniciara a las $1 horas . . ."

while : ; do
	if [ $(date +%H:%M) = "$1" ]; then
		break;
	fi
	sleep 30;
done

echo "Reiniciando . . ."
sleep 3;

reboot
