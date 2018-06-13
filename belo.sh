#!/usr/bin/env bash

bayeselo <<STDIN
readpgn /home/ghotrix/gdrive/t.pgn
elo
mm
exactdist
offset 2600
ratings >ratings.txt
STDIN

echo -e "\n"
cat ratings.txt
python gen_js_chart.py
