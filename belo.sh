#!/usr/bin/env bash

bayeselo <<STDIN
readpgn t.pgn
elo
mm
exactdist
offset 2271
ratings 20>ratings.txt
STDIN

echo -e "\n"
cat ratings.txt
python gen_js_chart.py
