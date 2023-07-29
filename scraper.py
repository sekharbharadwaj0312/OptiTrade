from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

link = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iPhone+10&_sacat=0&LH_TitleDesc=0&_sop=12"

def getData(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    results = soup.find_all('div', {'class':'s-item__info clearfix'})
    for item in results:
        products = {
            'title': item.find('span', {'class': 's-item__title'}).text, 
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$','').replace(',','').strip()),
            'solddate': item.find('span', {'class': 's-item__title--tag'}).find('span', {'class': 'POSITIVE'}).text,
            'bids': item.find('span', {'class': 's-item__bids'}).text, 
            'link': item.find('a', {'class': 's-item__link'})['href']
                }
        print(products)
    return

soup = getData(link)
parse(soup)