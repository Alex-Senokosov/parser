# pip install lxml
# pip install bs4
import re

from bs4 import BeautifulSoup
with open('index1.html') as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src,"lxml")


links = soup.find(class_="some__links").find_all("a")




find_a_by_text = soup.find_all(string=re.compile('([Оо]дежда)'))
print(find_a_by_text)


# find_a_by_text = soup.find("a", string=re.compile('Одежда'))
# print(find_a_by_text)


# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)


# for link in links:
#     link_href_attr= link.get("href")
#     link_fata_attr = link.get("data-attr")
#     print(f"href : {link_href_attr}--- data-attr : {link_fata_attr}")
# next_el = soup.find(class_="post__date").find_previous_sibling()
# print(next_el)
# next_el = soup.find(class_="post__title").find_next_sibling()
# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)

# post_div = soup.find(class_='post__text').find_parents("div",
# "user__post")
# print(post_div)
# post_div = soup.find(class_='post__text').find_parent("div",
# "user__post")
# print(post_div)

# post_div = soup.find(class_='post__text').find_parent()
# print(post_div)



# all_a = soup.find_all('a')
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f'{item_text}:{item_url}')

# social_links = soup.find(class_="social__networks").find(
#     'ul').find_all('a')
# print(social_links)



# user_name = soup.find("div",class_ = 'user__name').find('span').text
# print(user_name )



# user_name = soup.find("div",class_ = 'user__name')
# print(user_name.text.strip())

# title = soup.title
# print(title)
# # .find() .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_h1_all = soup.find_all("h1")
# print(page_h1_all)
#
# for item in page_h1_all:
#     print(item.text)