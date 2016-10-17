#!/bin/bash

if [ $# -ne "2" ]
then
  echo "Error: There must be exactly two parameters."
  echo "Usage: $0 [input dir] [output dir]"
  exit 1
fi

if [ ! -d "$1" ]
then
  echo "Error: \"$1\" is not a valid directory."
  echo "Usage: $0 [input dir] [output dir]"
  exit 1
fi

if [ ! -d "$2" ]
then
  echo "Error: \"$2\" is not a valid directory."
  echo "Usage: $0 [input dir] [output dir]"
  exit 1
fi

shopt -s nullglob

if [ -z "$(find $1 -maxdepth 1 -name '*.ui' -print -quit)" ]
then
  echo "Input directory was empty. Nothing to do."
  exit 0
fi

for f in $1/*.ui
do
  filename=$(basename "$f")
  filename="${filename%.*}"
  echo "Compiling \"$f\" -> \"$2/$filename.py\""
  pyuic5 "$f" -o "$2/$filename.py"
  if [ $? -ne 0 ]
  then
    echo "Error: A .ui file failed to compile. Exiting..."
    exit 1
  fi
done
