#!/usr/bin/env bash

for d in */ ; do
    echo $d
    for a in `ls -1 *.taz`; do gzip -dc $a | tar xf -; done
done