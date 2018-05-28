from bs4 import BeautifulSoup
import subprocess
import urllib.request

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

for index, a in enumerate(all_a):
    if not index % 4:
        save_as = a.get('download')
        href = a.get('href')
        url = base_url + href
        subprocess.run(["wget", url, "-N", "-nc", "-O", save_as])
