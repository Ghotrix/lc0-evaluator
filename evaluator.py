import glob
import re
from random import sample
from chess import pgn
import subprocess

tournament_pgn = 't.pgn'

weight_files = glob.glob('*.txt.gz')

weights = sorted([int(re.search('(.*)_(\d*)\.txt\.gz', file).group(2)) for file in weight_files])

try:
    with open(tournament_pgn) as pgn_file:
        pass
except FileNotFoundError:
    pass

rand_nets = sample(weights, 2)

#subprocess.run(['cutechess-cli', '-pgnout', tournament_pgn, '-engine', ])
