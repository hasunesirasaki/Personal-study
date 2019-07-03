import requests
import janome
from bs4 import BeautifulSoup

handle = ""
r = requests.get("https://twitter.com/"+handle)
