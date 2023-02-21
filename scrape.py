from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol><li class="special">This list item is special.</li>
  <li class="special">This list item is also special.</li>
  <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
# print(soup.head)
# print(soup.title)
# print(soup.title.get_text())
# print(soup.div.h3)
# print(soup.div.h3.get_text())
# print(soup.ol)
# print(soup.ol.li.get_text())
# print(soup.find_all(class_="special"))
# print(soup.find_all(class_='special')[1].text)
# print(soup.find_all(class_='special')[0].text)
# print(soup.ol.get_text())
# print(soup.div.h3)
# print(soup.div.h3.attrs['data-example'])
# print(soup.body.contents)
# print(soup.body.get_text())
# print(soup.body.contents[1])
