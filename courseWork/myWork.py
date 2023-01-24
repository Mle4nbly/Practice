import requests
from pprint import pprint
import json
import os

class PhotoInfo:
    def __init__(self, token: str, version='5.131'):
        self.token = token
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        self.url = 'https://api.vk.com/method/'

    def id_translate(self, user_id): #Метод для перевода ID пользователя в числовой вид.
        url = self.url + 'users.get'
        self.user_id = user_id
        params = {'user_ids': self.user_id}
        resp = requests.get(url, params={**self.params, **params})
        for user_info in resp.json()['response']:
            self.id = user_info['id']

    def photo_info(self): #Метод для получения информации по фотографиям.
        url = self.url + 'photos.get'
        params = {'owner_id': self.id, 'extended': 1, 'album_id': 'profile'}
        self.resp = requests.get(url, params={**self.params, **params})
        return self.resp.json()
                
class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, folder_name): #Метод для создания папки на ЯД.
        self.folder_name = folder_name
        self.path = {'path': self.folder_name}
        resp = requests.put(self.url, params=self.path, headers=self.headers)
        return resp.json()

    def photo_uploader(self): #Метод для загрузки фотографий на ЯД.
        url = self.url + '/upload'
        name_list = []
        value_for_json = []
        for_json = {}
        with open(os.path.join(os.path.dirname(__file__),'file_info.json'), 'w') as f:
            for photos_info in pi.resp.json()['response']['items']:
                sizes_list = []
                
                for photo_sizes in photos_info['sizes']:
                    sizes_list.append(photo_sizes['height'])
                
                for photo_sizes in photos_info['sizes']:
                    
                    if photo_sizes['height'] == max(sizes_list):
                        name_list.append(photos_info['likes']['count'])
                        counter = 0
                        
                        for name in name_list:
                            if name == photos_info['likes']['count']:
                                counter += 1

                        if counter > 1:
                            params = {
                                'path': f"{self.folder_name}/{photos_info['likes']['count']}{photos_info['date']}.jpg", 
                                'url': photo_sizes['url']
                                }
                            resp = requests.post(url, params=params, headers=self.headers)
                            pprint(resp.json())
                            value_for_json.append({
                                "file_name": f"{photos_info['likes']['count']}{photos_info['date']}.jpg", 
                                "size": f"{photo_sizes['height']}x{photo_sizes['width']}"
                                })
                            
                        else:
                            params = {
                                'path': f"{self.folder_name}/{photos_info['likes']['count']}.jpg",
                                'url': photo_sizes['url']
                                }
                            resp = requests.post(url, params=params, headers=self.headers)
                            pprint(resp.json())
                            value_for_json.append({
                                "file_name": f"{photos_info['likes']['count']}.jpg", 
                                "size": f"{photo_sizes['height']}x{photo_sizes['width']}"
                                })

            for_json["items"] = value_for_json       
            json.dump(for_json, f, ensure_ascii=False, indent=4)
                    
if __name__ == '__main__':
    user_id = input('ID вашего профиля:')
    ya_token = input('Введите ключ ЯД API:')
    folder_name = input('Введите название папки на ЯД, в которую хотите сохранить фотографии(Если нет папки просто нажмите Enter):')
    vk_token = input('Введите ключ VK API:')
    pi = PhotoInfo(token=vk_token)
    yu = YaUploader(token=ya_token)
    yu.create_folder(folder_name=folder_name)
    pi.id_translate(user_id=user_id)
    pprint(pi.photo_info())
    pprint(yu.photo_uploader())