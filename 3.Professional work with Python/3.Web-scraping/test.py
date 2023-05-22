import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

#test code

headers = Headers(browser='firefox', os='win')

html_data = requests.get('https://www.iplocation.net/', headers=headers.generate()).text
# print(html_data)

soup = BeautifulSoup(html_data, 'lxml')

tag_div = soup.find('div', id='ip-placeholder')

tag_p = tag_div.find_all('p')[0]

tag_span = tag_p.find_all('span')[0]

print(tag_span.text)


