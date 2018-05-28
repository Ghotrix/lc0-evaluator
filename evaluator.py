import glob
import re
import os
from random import sample, choice
from chess import pgn
import subprocess


def get_least_played(players, weights):
    least_played = [k for k, v in players.items() if v == players[min(players, key=players.get)]]
    if len(least_played) == 1:
        weights.remove(least_played[0])
        least_played.append(choice(weights))
        weights.append(least_played[0])
    print('least played nets: {}'.format(least_played))
    return least_played


tournament_pgn = 't.pgn'

weight_files = glob.glob('*.txt.gz')

weights = sorted([int(re.search('(.*)_(\d*)\.txt\.gz', file).group(2)) for file in weight_files])

players = {}
for weight in weights:
    players[weight] = 0

try:
    with open(tournament_pgn) as pgn_file:
        while True:
            game = pgn.read_game(pgn_file)
            if game is None:
                break
            wh = int(game.headers['White'])
            bl = int(game.headers['Black'])

            players[wh] += 1
            players[bl] += 1
except FileNotFoundError:
    pass

cur_dir = os.getcwd()

for i in range(0, 500):
    least_played = get_least_played(players, weights)
    rand_nets = sample(least_played, 2)
    players[rand_nets[0]] += 1
    players[rand_nets[1]] += 1
    print('game will be played between {} and {}'.format(rand_nets[0], rand_nets[1]))
    result = subprocess.run('cutechess-cli -pgnout {3} -engine name={0} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{0}.txt.gz" -engine name={1} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{1}.txt.gz" \
                             -each proto=uci nodes=800 tc=inf'.format(rand_nets[0], rand_nets[1],
                                                                      cur_dir, tournament_pgn),
                            stdout=subprocess.PIPE, shell=True)
