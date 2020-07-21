from bs4 import BeautifulSoup
import requests

url="https://news.google.co.in/"
code=requests.get(url)
soup=BeautifulSoup(code.text,'html5lib')
for title in soup.find_all('span',class_="titletext"):
    print(title.text)