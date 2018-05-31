import glob
import re
import os
from random import sample, choice
#from chess import pgn
import subprocess
import bisect
from collections import OrderedDict


def get_near_points_opponent(player, players):
    points_value = players[player][1]
    ordered_players = OrderedDict(sorted(players.items(), key=lambda t: t[1][1]))
    del ordered_players[player]
    weights = []
    points = []
    for weight, stats in ordered_players.items():
        weights.append(weight)
        points.append(stats[1])
    near_point = bisect.bisect_left(points, points_value)
    try:
        return weights[near_point]
    except IndexError:
        return choice(weights)


def get_least_played_equal_opponents(players):
    least_played = [[k, v[1]] for k, v in players.items() if v[0] == players[min(players, key=players.get)]]
    equal_opponents = []
    if len(least_played) == 1:
        least_played.append(get_near_points_opponent(least_played[0], players))
    print('least played nets: {}'.format(least_played))
    return least_played


def get_points_from_result(result):
    points = float('nan')
    if result == '1-0':
        points = 1.
    elif result == '0-1':
        points = 0.
    elif result == '1/2-1/2':
        points = 0.5

    return points


'''tournament_pgn = 't.pgn'

weight_files = glob.glob('*.txt.gz')

weights = sorted([int(re.search('(.*)_(\d*)\.txt\.gz', file).group(2)) for file in weight_files])

players = {}
for weight in weights:
    players[weight] = [0, 0]  # games played, points gathered

try:
    with open(tournament_pgn) as pgn_file:
        while True:
            game = pgn.read_game(pgn_file)
            if game is None:
                break

            wh = int(game.headers['White'])
            bl = int(game.headers['Black'])
            points = get_points_from_result(game.headers['Result'])

            players[wh][0], players[wh][1] = players[wh][0] + 1, players[wh][1] + points
            players[bl][0], players[bl][1] = players[bl][0] + 1, players[bl][1] + 1 - points
except FileNotFoundError:
    pass

cur_dir = os.getcwd()

while True:
    least_played = get_least_played_equal_opponents(players)
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
'''

if __name__ == '__main__':
    players = {1: [2, 1], 2: [3, 0], 3: [2, 0], 4: [2, 2]}
    x = get_near_points_opponent(2, players)
    print(x)
