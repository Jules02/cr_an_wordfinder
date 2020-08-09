#!/usr/bin/env bash

for d in *.taz; do tar xaf $d; done && for d in *.tar; do tar -xvf $d; done && rm -rf AAA* && rm -rf *.tar  && rm -rf *.taz