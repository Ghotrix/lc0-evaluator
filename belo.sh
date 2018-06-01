#!/usr/bin/env bash

bayeselo <<STDIN
readpgn t2.pgn
elo
mm
exactdist
offset 2599
ratings >ratings.txt
STDIN

echo -e "\n"
cat ratings.txt
python gen_js_chart.py
