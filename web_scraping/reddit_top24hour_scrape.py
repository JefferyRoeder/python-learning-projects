from bs4 import BeautifulSoup
from requests import get
from fake_useragent import UserAgent

ua = UserAgent()

def lovely_soup(u):
    r = get(u, headers={'User-Agent': ua.chrome})
    return BeautifulSoup(r.text, 'lxml')

# soup = lovely_soup('https://old.reddit.com/top/?sort=top&t=day')
# thing = soup.find('div',{'class':'subtitle'})
# print(thing)



def get_headlines():
    soup = lovely_soup('https://www.copypress.com/blog/40-headlines-the-good-the-bad-and-the-ugly/')
    headlines = soup.find('div', {'class': 'blog-single-inner-cont'})
    headlines = headlines.findall('strong')

    for headline in headlines[1:]:
        line = headline.text
        line = line.lstrip('0123456789.- ').strip()
        print(line)

get_headlines()