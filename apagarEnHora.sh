while : ; do

	if [ $(date +%H:%M) = "$1" ]; then
		break;
	fi
done
echo "Apagando . . ."
sleep 4;
poweroff
