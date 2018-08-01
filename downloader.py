from bs4 import BeautifulSoup
import subprocess
import urllib.request
import re
import os, os.path
import json

bayes_players_path = 'ccrl/players.txt'
bayes_engines_path = 'ccrl/engines.json'

lc0_engine_template = { 'name': '', 'command': 'lc0', 'protocol': 'uci', 'options': [ \
    {'name':'Network weights file path', 'value':''}, \
    {'name':'Initial temperature', 'value':1}, \
    {'name':'Moves with temperature decay', 'value': '12'} \
    ] }

try:
    with open('bad_nets.txt', 'r') as bad_nets_file:
        bad_nets = list(bad_nets_file)
        bad_nets = [int(x) for x in bad_nets]
except:
    raise('Cannot read file with the list of bad nets')

good_nets = {'t': [x for x in range(10400, 10261, -1)], 'm': [521, 527]}#x for x in range(505, 495, -10)] + [125, 120, 115], 'o': [75, 27, 64]}
#good_nets = {'t': [x for x in range(9232, 9020, -10)], 'm': [], 'o': [75, 27, 64]}
#good_nets = {'t': [27, 64, 75] + [x for x in range(4046, 4015, -5)], 'm': [], 'o': [75, 27, 64]}

base_urls = {'t': 'http://testserver.lczero.org', 'm': 'http://lczero.org'}
for k, base_url in base_urls.items():
    url = '{}/networks'.format(base_url)
    req = urllib.request.Request(
        url,
        data=None,
        headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    html_data = None
    with urllib.request.urlopen(req) as response:
        html_data = response.read().decode('utf-8')

    soup = BeautifulSoup(html_data, 'html.parser')
    all_a = soup.find_all('a', {'class': ''})


    for a in all_a:
        save_as = a.get('download')
        net_number = int(re.search('(.*)_(\d*)\.txt\.gz', save_as).group(2))
    
        #if net_number < 23 or (net_number % 3 != 0 and net_number not in good_nets):
        #    continue
        if net_number not in good_nets[k]:
            continue
        if net_number in bad_nets:
            continue
        href = a.get('href')
        url = base_url + href

        if not os.path.isfile(os.path.join(os.getcwd(), 'weights_{}.txt.gz'.format(net_number))):
            full_bayes_path = os.path.join(os.getcwd(), bayes_players_path)
            full_engines_path = os.path.join(os.getcwd(), bayes_engines_path)
            lc0_net_present = False
            lc0_engine_present = False

            engines_list = []

            with open(full_bayes_path, 'r') as bayes_players_file:
                for line in bayes_players_file:
                    if 'LC0 16.{}'.format(net_number) in line:
                        lc0_net_present = True
                        break
            if not lc0_net_present:
                with open(full_bayes_path, 'a') as bayes_players_file:
                    bayes_players_file.write('LC0 16.{}\n'.format(net_number))

            with open(full_engines_path, 'r') as bayes_engines_file:
                engines_list = json.load(bayes_engines_file)
                for engine in engines_list:
                    if 'LC0 16.{}'.format(net_number) in engine['name']:
                        lc0_engine_present = True
                        break

            if not lc0_engine_present:
                with open(full_engines_path, 'w') as bayes_engines_file:
                    lc0_engine = lc0_engine_template
                    lc0_engine['name'] = 'LC0 16.{}'.format(net_number)
                    for option in lc0_engine['options']:
                        if 'Network' in option['name']:
                            option['value'] = '/home/ghotrix/PycharmProjects/leela_evaluator/weights_{}.txt.gz'.format(net_number)
                            break
                    engines_list.append(lc0_engine)
                    json.dump(engines_list, bayes_engines_file)

        subprocess.run(["wget", url, "-nc", "-O", 'weights_{}.txt.gz'.format(net_number)])
