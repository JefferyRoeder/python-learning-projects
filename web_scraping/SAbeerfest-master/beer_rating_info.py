import bs4 as bs
import urllib.request
import csv
import pandas as pd
source = urllib.request.urlopen('https://untappd.com/beer/top_rated?type=adambier').read()
soup = bs.BeautifulSoup(source,'lxml')
f = csv.writer(open('beers.csv','w'))
body = soup.body    
table = soup.find_all("div",{"class":"beer-item"})
#table_rows = table.find_all('span',{"class":"num"})
for t in table:
    beer_rating = []
    rating = t.select('span',{"class":"num"})
    name = t.select('a',{"class":"name"})
    row_rating = [i.text for i in rating]
    row_name = [i.text for i in name]
    #f.writerow(rating)
    #print(row_name[1])
    #beer_rating = beer_rating.append([[row_name[1],row_rating[1]]])
    print(row_name[1],row_rating[1])