import requests
from bs4 import BeautifulSoup
URL = "http://quotes.toscrape.com/"
html = requests.get(URL)
soup = BeautifulSoup(html.text, "html.parser")

while True:
    for i in soup.find_all(class_="quote"):
        print(i.find(class_="text").text)
        print(i.find(class_="author").text)
        print('###############################')
    nextlink = soup.find(class_="next")
    if nextlink:
        nextlink = URL + nextlink.a['href']
        subhtml = requests.get(nextlink)
        soup = BeautifulSoup(subhtml.text, "html.parser")
    else:
        break