#!/bin/bash

if [[ $2 == "r" ]];then
	systemctl start $1
	systemctl status $1
fi

if [[ $2 == "s" ]];then
	systemctl stop $1
	systemctl status $1
fi

if [[ $2 == "re" ]];then
	bash tools.sh $1 s
	bash tools.sh $1 r
fi



