from bs4 import BeautifulSoup
import urllib.request

url = "http://www.websitesi.com"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')

icerik = soup.find_all('span',attrs={'id':'offering-price'})

baslik = soup.find_all('title')
print(baslik[0].text)
print(icerik)
