import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://kbsu.ru/news/'


def get_info(url_id):
    req = requests.get(url_id)
    src = req.content

    soup = BeautifulSoup(src, 'lxml')

    category_list_item = soup.find_all(class_='category-list__item')

    posts_list = []

    for item in category_list_item:
        title = item.find('a', class_='category-list__item__title').text.strip()
        short_desc = item.find(class_='category-list__item__excerpt').text.strip()
        date = item.find(class_='category-list__item__date').text.strip()

        posts_list.append(
            [title, short_desc, date]
        )

    print(posts_list)

    for posts in posts_list:
        for key in posts:
            print(key)

            with open('data/data.txt', 'a', encoding='utf-8') as file:
                file.write(key)
                file.write('\n')
        with open('data/data.txt', 'a', encoding='utf-8') as file:
            file.write('\n')


for i in range(1, 158):
    get_info(url + 'page/' + str(i) + '/')
