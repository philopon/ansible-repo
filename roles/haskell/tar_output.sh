#!/usr/bin/env bash

result=`tar tf $1 | head -n 1`
echo ${result%%/*}
