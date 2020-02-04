#SA Beerfest WebScrape
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# Targeting beer name, brewery, tyoe of beer, pulling from SAbeerfest.com
url= 'https://sanantoniobeerfestival.com/mobile/'
response = requests.get(url)


