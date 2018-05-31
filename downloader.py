from bs4 import BeautifulSoup
import subprocess
import urllib.request
import re

base_url = 'http://lczero.org'
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

bad_nets = [250]
good_nets = [345, 237, 355]

for a in all_a:
    save_as = a.get('download')
    net_number = int(re.search('(.*)_(\d*)\.txt\.gz', save_as).group(2))

    if net_number < 126 or (net_number % 4 != 0 and net_number not in good_nets):
        continue
    print(net_number)
    if net_number in bad_nets:
        bad_nets.remove(net_number)
        net_number -= 1
    href = a.get('href')
    url = base_url + href
    subprocess.run(["wget", url, "-nc", "-O", 'weights_{}.txt.gz'.format(net_number)])
