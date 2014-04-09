#!/usr/bin/env bash
# cabal: The directory "alex-3.1.3/" already exists, not unpacking.
# Unpacking to alex-3.1.3/
cabal get $1 -d $2 2>&1 | awk '$1 == "Unpacking" { print $3 } $3 == "directory" { print substr($4,2,length($4) - 2) }'

