from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_currency):
  url = f'https://www.xe.com/de/currencyconverter/convert/?Amount=1&From={in_currency}&To={out_currency}'
  print(url)
content = requests.get(url.text)
soup = BeautifulSoup(content,'html.parser')
soup = soup.find()
get_currency('INR','EUR')