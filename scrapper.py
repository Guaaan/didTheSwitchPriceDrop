import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

# ripley
#def check_price_ripley():
url = 'https://simple.ripley.cl/consola-nintendo-switch-neon-color-new-model-sniper-mpm00016486196?gclid=EAIaIQobChMI_6buhLDh9QIVwYORCh1wxQzfEAQYASABEgK8oPD_BwE&s=mdco'
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# title = soup.find(aui el titulo de del producto en caso de ser necesario).get_text()
normalPrice = soup.find_all(class_="product-price").__getitem__(0).get_text()
internetPrice = soup.find_all(class_="product-price").__getitem__(1).get_text()

normalPrice = normalPrice.replace('$', '')
normalPrice = normalPrice.replace('.', '')
internetPrice = internetPrice.replace('$', '')
internetPrice = internetPrice.replace('.', '')

ripley = {
    'normal': int(normalPrice),
    'internet': int(internetPrice)
}

print(ripley)
        
