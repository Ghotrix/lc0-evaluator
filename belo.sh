#!/usr/bin/env bash

bayeselo <<STDIN
readpgn t.pgn
elo
mm
exactdist
offset 2730
ratings >ratings.txt
STDIN

echo -e "\n"
cat ratings.txt
python gen_js_chart.py
