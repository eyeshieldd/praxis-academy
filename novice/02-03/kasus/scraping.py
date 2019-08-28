from bs4 import BeautifulSoup
import requests

page = requests.get('https://mojok.co')
soup = BeautifulSoup(page.text, 'html.parser')
if page.status_code==200:
    div = soup.find(id='cb-section-lp')

articles = div.find_all('article')
for a in articles:
    single = a.find('h2')
    print(single.find('a').text)