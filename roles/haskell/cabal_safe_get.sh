#!/usr/bin/env bash

get=`cabal get $1 -d $2`

if [ $? -eq 0 ]; then
  echo $get | awk 'NR == 1{ print $3 }'
else
  echo $get | awk 'BEGIN{ FS = "\""} NR == 1 { print $2 }'
fi

