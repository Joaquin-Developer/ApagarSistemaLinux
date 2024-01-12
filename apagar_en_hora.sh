#!/bin/bash

echo "El sistema se apagará a las $1 horas . . ."

while : ; do
	if [ $(date +%H:%M) = "$1" ]; then
		break;
	fi
	sleep 30;
done

echo "Apagando . . ."
sleep 4;

poweroff
