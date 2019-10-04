import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.basketball-reference.com/players/d/duncati01.html#all_per_game').read()


soup = bs.BeautifulSoup(source,'lxml')

body = soup.body    
table = soup.select('#per_game')
table_rows = table[0].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]

    print(row)