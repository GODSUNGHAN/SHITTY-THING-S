import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import Request, urlopen
import re

html = Request ("https://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0")
webpage = urlopen(html).read()
soup = BeautifulSoup(webpage, "html.parser")
my_titles = soup.find_all(href=re.compile(""))
print(my_titles)

data = {}


for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)