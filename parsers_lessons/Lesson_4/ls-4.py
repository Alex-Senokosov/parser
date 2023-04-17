import requests
from bs4 import BeautifulSoup
import json
persons_url_list = []
headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
 }
for i in range(0, 740, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={i}'
    q = requests.get(url,headers=headers)
    result = q.text
    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all(class_='bt-slide-content')
    person_page_url =[i.findChild('a')['href'] for i in persons]
    persons_url_list.append(person_page_url)
with open('persons_url_list.txt', 'a') as file:
    for line in persons_url_list:
        file.write(f'{line}\n')