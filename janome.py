from bs4 import BeautifulSoup

from janome.tokenizer import Tokenizer
import requests

URL = "https://toyokeizai.net/articles/print/227362"
buf = requests.get(URL)
soup = BeautifulSoup(buf.content,"lxml")
data = MyHtmlStripper(str(soup.find(id="article-body-inner"))).value

t = Tokenizer()
tokens = t.tokenize(data)
tokenlist =[]
for token in tokens:
    if token.part_of_speech.split(",")[0] =="名詞":
        if token.part_of_speech.split(",")[1] != "非自立" and \
        token.part_of_speech.sprit(",")[1] !="接尾" :
            tokenlist.append(token.base_form)
            print(token)
from collections import Counter
c = Counter(tokenlist)
print(c.most_common())
