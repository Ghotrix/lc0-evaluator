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


def sample_two_equal_opponents(weight_points, fixed_opponent=None):
    if fixed_opponent:
        random_weight = fixed_opponent
    else:
        random_weight = choice(weight_points)

    ordered_by_points = sorted(weight_points, key=get_game_point_ratio)
    print(ordered_by_points)
    first_idx = ordered_by_points.index(random_weight)
    second_idx = first_idx + 1
    if second_idx >= len(ordered_by_points):
        return [ordered_by_points[first_idx][0], ordered_by_points[second_idx - 2][0]]
    else:
        return [ordered_by_points[first_idx][0], ordered_by_points[second_idx][0]]


def get_least_played_equal_opponents(players):
    least_played = [[k, v[0], v[1]] for k, v in players.items()
                    if v[0] == min(players.items(), key=lambda x: x[1][0])[1][0]]
    rest_played = [[k, v[0], v[1]] for k, v in players.items() if [k, v[0], v[1]] not in least_played]

    if len(least_played) == 1:
        rest_played += least_played
        equal_opponents = sample_two_equal_opponents(rest_played, least_played[0])
        print('least played equal-ish nets: {}'.format(equal_opponents))
        return equal_opponents
    equal_opponents = sample_two_equal_opponents(least_played)
    print('least played equal-ish nets: {}'.format(equal_opponents))
    return equal_opponents


def get_points_from_result(result):
    print('got {} result'.format(result))
    points = float('nan')
    if result in ['1-0', '1']:
        points = 1.
    elif result in ['0-1', '0']:
        points = 0.
    elif result in ['1/2-1/2', '1/2']:
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
            if wh not in weights or bl not in weights:
                continue
            points = get_points_from_result(game.headers['Result'])

            players[wh][0], players[wh][1] = players[wh][0] + 1, players[wh][1] + points
            players[bl][0], players[bl][1] = players[bl][0] + 1, players[bl][1] + 1 - points
except FileNotFoundError:
    pass

cur_dir = os.getcwd()

while True:
    least_played = get_least_played_equal_opponents(players)
    white_weight = least_played[0]
    black_weight = least_played[1]
    print('game will be played between {} with {} games and {} points and {} with {} games and {} points'.format(white_weight, players[white_weight][0], players[white_weight][1], black_weight, players[black_weight][0], players[black_weight][1]))
    result = subprocess.run('cutechess-cli -pgnout {3} -engine name={0} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{0}.txt.gz" -engine name={1} cmd=./lc0.sh \
                             arg="--weights={2}/weights_{1}.txt.gz" \
                             -each proto=uci nodes=800 tc=inf'.format(white_weight, black_weight,
                                                                      cur_dir, tournament_pgn),
                            stdout=subprocess.PIPE, shell=True)
    result = result.stdout.decode('ascii')
    found = re.search('(.*)\): (.*)-(.*) \{(.*)', result)
    players[white_weight][0] += 1
    players[black_weight][0] += 1
    players[white_weight][1] += get_points_from_result(found.group(2))
    players[black_weight][1] += get_points_from_result(found.group(3))
    print('current result of player {} is: {}'.format(white_weight, players[white_weight][1]))
    print('current result of player {} is: {}'.format(black_weight, players[black_weight][1]))
