#!/bin/sh

for i in $( ls examples); do
	echo sheepda $i	
	if [ "${i#*.}" = "da" ]; then 
    	sheepda examples/$i
	fi
done
