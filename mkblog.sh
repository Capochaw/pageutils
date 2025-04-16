#!/bin/bash

archivo="$1"
carpe="$2"

if [ "$carpe" = "" ]; then
	pandoc "${archivo}" \
	  --to=html5 \
	  --standalone \
	  --template="/home/capocha/doc/code/page/temps/blogtemp.html" \
	  -o "/home/capocha/doc/code/page/blog/${archivo::-3}.html"
else
	if [ ! -d /home/capocha/doc/code/page/blog/$carpe ]; then
		mkdir /home/capocha/doc/code/page/blog/$carpe
	fi
	pandoc "${archivo}" \
	  --to=html5 \
	  --standalone \
	  --template="/home/capocha/doc/code/page/temps/blogtemp.html" \
	  -o "/home/capocha/doc/code/page/blog/${2}/${archivo::-3}.html"
fi

python3 ~/doc/code/pagemode/autoblog.py
