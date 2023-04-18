import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent
from tqdm import tqdm

ua = UserAgent()
headers = {
        "Accept": "*/*",
        "User-Agent": ua.random
 }

person_url_list = []
for i in range(0, 740, 12):
    url = f"https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=12&noFilterSet=true&offset={i}"
    print(f"Страница {url} взята в разработку")
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        persons = soup.find_all(class_="bt-slide-content")
        for person in persons:
            person_page_url = person.find("a").get("href")
            person_url_list.append(person_page_url)
            print(f"На странице {url} найдена и записана ссылка {person_page_url}")
        print(f"Страница {url} обработана")
    else:
        print(f"Error requesting URL: {url}, status code: {response.status_code}")

with open('person_url_list.txt', 'a') as file:
    for line in person_url_list:
        file.write(f'{line}\n')

headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
 }

with open("person_url_list.txt") as file:
    lines = [line.strip() for line in file.readlines()]

data_dict = []
count = 0

for line in tqdm(lines, desc="Процесс"):
    q = requests.get("https://www.bundestag.de"+line, headers=headers, proxies={'https': 'http://r894QHkE:nivYKzJG@45.149.131.202:63182'})
    result = q.text
    soup = BeautifulSoup(result, "lxml")
    person = soup.find(class_="bt-biografie-name").find("h3").text
    person_name_company = person.strip().split(",")
    person_name = person_name_company[0]
    person_company = person_name_company[1].strip()
    social_network = soup.find_all(class_="bt-link-extern")
    social_network_url = []

    for item in social_network:
        social_network_url.append(item.get('href'))
    count += 1
    data = {
        "Person_name": person_name,
        "Person_company": person_company,
        "Person_social_url": social_network_url
    }
    data_dict.append(data)
    print(f"#{count}:{line} done")

with open('data.json', "w") as json_file:
    json.dump(data_dict, json_file,indent=4)
print("Завершено")
