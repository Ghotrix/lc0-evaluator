#!/usr/bin/env bash

lc0 $@ --minibatch-size=512 --extra-virtual-loss=0.4 --temperature=0.5 --tempdecay-moves=5

