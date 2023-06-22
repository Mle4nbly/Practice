import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import os
import json


def get_headers():
    return Headers(browser="firefox", os="win").generate()

def get_text(url):
    return requests.get(url=url, headers=get_headers()).text


def hh_parser(url):
    html = get_text(url)
    soup = BeautifulSoup(html,'lxml')
    if soup.find('div',id='a11y-main-content') == None:
        return
    all_vacancies = soup.find('div',id='a11y-main-content').find_all('div', class_='serp-item')
    for vacancy in all_vacancies:
        title = vacancy.find(class_='serp-item__title')
        link = title["href"]
        city = vacancy.find(class_='vacancy-serp-item__info').find(attrs = {'data-qa': 'vacancy-serp__vacancy-address'}).text
        company = vacancy.find(class_='vacancy-serp-item-company').find(class_='bloko-link bloko-link_kind-tertiary').text
        if vacancy.find('span',class_='bloko-header-section-3') == None:
            salary = 'Не указано'
        else:
            salary = vacancy.find('span',class_='bloko-header-section-3').text
        vacancy_data.append({
            'link': link,
            'salary': salary,
            'company': company,
            'city': city
        })
    

def writing_to_json():
    with open(os.path.join(os.path.dirname(__file__),'vacancies.json'), 'w', encoding='utf8') as f:
        data_for_json['items'] = vacancy_data
        json.dump(data_for_json, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    data_for_json = {}
    vacancy_data = []
    for page in range (0, 10):
        url = f'https://spb.hh.ru/search/vacancy?text=junior+python&area=1&area=2&page={page}'
        hh_parser(url=url)
    writing_to_json()