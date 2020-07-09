from bs4 import BeautifulSoup as BS
from lxml import html
import requests

def soupify(weburl, bag):
    page = requests.get(weburl, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BS(page.text, 'lxml')

    # allbags = soup.find_all('h3', {'class':'product-item-name'})
    allbags = soup.find_all('li', {'product-grid-list-item ng-star-inserted'})
    for b in allbags:
        print(b.text)
    


if __name__ == "__main__":
    target = "https://www.hermes.com/us/en/category/women/bags-and-small-leather-goods/bags-and-clutches/"
    bagname = "lindy"
    soupify(target, bagname)