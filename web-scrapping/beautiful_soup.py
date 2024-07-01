import requests
from bs4 import BeautifulSoup

# "-------------------------BUSINESS----------------------------------------"
# target url
url = 'https://www.cnn.com'

res = requests.get(url)
html_content = res.content
# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')
print(soup)

headings = soup.find_all(['h1', 'h2'])


f = open("results.txt", 'w')

for heading in headings:
    f.write(heading.get_text())
