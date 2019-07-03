import requests
from bs4 import BeautifulSoup

URL = "http://blog.media.teu.ac.jp/"

data = requests.get(URL)
soup = BeautifulSoup(data.text,"lxml")

print(soup.find_all("img"))
