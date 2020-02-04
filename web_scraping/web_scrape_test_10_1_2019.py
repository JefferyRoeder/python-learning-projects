import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()


soup = bs.BeautifulSoup(source,'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))