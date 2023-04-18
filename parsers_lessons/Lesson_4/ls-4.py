import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
        "Accept": "*/*",
        "User-Agent": ua.random
 }

person_url_list = []
for i in range(0, 740, 12):
    url = f"https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=12&noFilterSet=true&offset=12"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        persons = soup.find_all(class_="bt-slide-content")
        for person in persons:
            person_page_url = person.find("a").get("href")
            person_url_list.append(person_page_url)
    else:
        print(f"Error requesting URL: {url}, status code: {response.status_code}")
with open('person_url_list.txt', 'a') as file:
    for line in person_url_list:
        file.write(f'{line}\n')


with open("person_url_list.txt") as file:
    lines = [line.strip() for line in file.readlines()]

data_dict = []
count = 0

for line in lines:
    q = requests.get(line,headers=headers)
    result = q.text
    soup = BeautifulSoup(result, "lxml")
    print(soup)
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
