import glob
import re
import os
from random import choice
from chess import pgn
import subprocess

def get_game_point_ratio(wnp):
    games_num = wnp[1]
    points = wnp[2]
    if games_num == 0:
        return 1.
    else:
        return points/float(games_num)


def sample_two_equal_opponents(weight_points):
    random_weight = choice(weight_points)

    ordered_by_points = sorted(weight_points, key=get_game_point_ratio)
    first_idx = ordered_by_points.index(random_weight)
    second_idx = first_idx + 1
    if second_idx >= len(ordered_by_points):
        return [ordered_by_points[first_idx], ordered_by_points[second_idx - 2]]
    else:
        return [ordered_by_points[first_idx], ordered_by_points[second_idx]]


def get_least_played_equal_opponents(players):
    least_played = [[k, v[0], v[1]] for k, v in players.items()
                    if v[0] == min(players.items(), key=lambda x: x[1][0])[1][0]]
    rest_played = [[k, v[0], v[1]] for k, v in players.items()] - least_played

    if len(least_played) == 1:
        least_played += [choice(rest_played)]
        assert len(least_played == 2)
        return [w for w, n, p in least_played]
    equal_opponents = sample_two_equal_opponents(least_played)
    print('least played equal-ish nets: {}'.format(equal_opponents))
    return equal_opponents


def get_points_from_result(result):
    points = float('nan')
    if result == '1-0':
        points = 1.
    elif result == '0-1':
        points = 0.
    elif result == '1/2-1/2':
        points = 0.5

    return points


tournament_pgn = 't.pgn'

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
    players[least_played[0]][0] += 1
    players[least_played[1]][0] += 1
    print('game will be played between {} and {}'.format(least_played[0], least_played[1]))
    result = subprocess.run('cutechess-cli -pgnout {3} -engine name={0} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{0}.txt.gz" -engine name={1} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{1}.txt.gz" \
                             -each proto=uci nodes=800 tc=inf'.format(least_played[0], least_played[1],
                                                                      cur_dir, tournament_pgn),
                            stdout=subprocess.PIPE, shell=True)
