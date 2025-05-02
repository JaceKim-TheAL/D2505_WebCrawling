import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
print(response)

html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

print(soup.select_one("head > title").text)

