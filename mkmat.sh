#!/bin/bash

archivo="$1"
carpe="$2"


if [ "$carpe" = "" ]; then
pandoc "${archivo}" \
  --to=html5 \
  --standalone \
  --mathjax \
  --template=/home/capocha/doc/code/page/temps/mattemp.html \
  -o "/home/capocha/doc/code/page/mat/post/${archivo::-3}.html"
else
pandoc "${archivo}" \
  --to=html5 \
  --standalone \
  --mathjax \
  --template=/home/capocha/doc/code/page/temps/mattemp.html \
  -o "/home/capocha/doc/code/page/mat/post/${carpe}/${archivo::-3}.html"
fi

python3 ~/doc/code/pagemode/automat.py

# pandoc entradas/${archivo} \
  # --pdf-engine=pdflatex \
  # --template=templates/latex.tex \
  # -o output/${archivo::-3}.pdf

