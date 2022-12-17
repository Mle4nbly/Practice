import requests
from pprint import pprint

#1 задание

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)

def get_status_request():
    pprint(resp.json())

def find_id_superhero(hero_name):
    for hero_info in resp.json():
        if hero_info['name'] == hero_name:
            pprint(f"{hero_name} ID - {hero_info['id']}")

def comparision_of_superhero(powerstat):
    id_list = [149,332,655]
    attribute_dict = {}
    for id in id_list:
        for hero_info in resp.json():
            if hero_info['id'] == id:
                attribute_dict[hero_info['name']] = hero_info['powerstats'][powerstat]
    for name in attribute_dict:
        if attribute_dict[name] == max(attribute_dict.values()):
            print(f'Наибольший показатель {powerstat} у {name} - {attribute_dict[name]}')

if __name__ == '__main__':
#    get_status_request()
#    find_id_superhero()
    comparision_of_superhero('speed')

#2 задание


