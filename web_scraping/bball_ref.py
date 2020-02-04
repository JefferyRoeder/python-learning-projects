import bs4 as bs
import urllib.request
import csv
import pandas as pd
source = urllib.request.urlopen('https://www.basketball-reference.com/players/d/duncati01/gamelog/2015').read()


soup = bs.BeautifulSoup(source,'lxml')

f = csv.writer(open('bball_ref.csv','w'))

body = soup.body    
table = soup.select('#pgl_basic')
table_rows = table[0].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]

    f.writerow(row)


with open('bball_ref.csv') as csvfile:
    bball_ref = csv.reader(csvfile,delimiter=",")
    rows = []
    for row in bball_ref:
        rows.append(row)

bball_ref_df = pd.DataFrame(rows)
bball_ref_df.loc[:,11:].head()
bball_ref_df = bball_ref_df.drop(columns=bball_ref_df.loc[:,29:])
bball_ref_df
bball_ref_df.columns = headers
bball_ref_df