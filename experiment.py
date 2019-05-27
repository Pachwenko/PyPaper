import requests
from bs4 import BeautifulSoup

page = requests.get('https://unsplash.com/t/wallpapers')

print(page.content)

soup = BeautifulSoup(page.content, "html.parser")

#
# for image in soup.find_all('img', src=True):
#     print(image['src'])


from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://unsplash.com/t/wallpapers')
r.html.render()

page2 = BeautifulSoup(r.content, 'html.parser')

for item in page2.find_all('img', src=True):
    print(item['src'])