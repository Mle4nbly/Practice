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

    def photo_info(self, user_id): #Метод для получения информации по фотографиям.
        url = self.url + 'users.get'
        params = {'user_ids': user_id}
        resp = requests.get(url, params={**self.params, **params})
        for user_info in resp.json()['response']:
            client_id = user_info['id']
        url = self.url + 'photos.get'
        params = {'owner_id': client_id, 'extended': 1, 'album_id': 'profile'}
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
        self.path = {'path': folder_name}
        resp = requests.put(self.url, params=self.path, headers=self.headers)
        return resp.json()

    def photo_uploader(self, folder_name, dict_for_upload: dict): #Метод для загрузки фотографий на ЯД.
        url = self.url + '/upload'
        for key in dict_for_upload.keys():
            params ={
                    'path': f"{folder_name}/{key}",
                    'url': f"{dict_for_upload[key]['url']}"
                    }
            resp = requests.post(url, params=params, headers=self.headers)
            pprint(resp.json())
            
class OtherLogic:
    def photo_selection(self):
        self.dict_for_upload = {}
        for photo_info in pi.resp.json()['response']['items']:
            height = 0
            counter = 0
            for photo_size in photo_info['sizes']:
                if height < photo_size['height']:
                    height = photo_size['height']
                    size = f"{photo_size['height']}x{photo_size['width']}"
                    url = photo_size['url']
            for key in self.dict_for_upload.keys():
                if photo_info['likes']['count'] == key:
                    self.dict_for_upload[f"{photo_info['likes']['count']}_{photo_info['date']}"] = {'size': size, 'url': url}
                    counter += 1
            if counter == 0:
                self.dict_for_upload[f"{photo_info['likes']['count']}"] = {'size': size, 'url': url}
    
    def file_info(self):
        for_json = {}
        value_for_json = []
        with open(os.path.join(os.path.dirname(__file__),'file_info.json'), 'w') as f:
            for key in self.dict_for_upload.keys():
                value_for_json.append({
                    "file_name": f"{key}", 
                    "size": f"{self.dict_for_upload[key]['size']}"
                })
            for_json['items'] = value_for_json
            json.dump(for_json, f, ensure_ascii=False, indent=4)
                
if __name__ == '__main__':
    user_id = input('ID вашего профиля:')
    ya_token = input('Введите ключ ЯД API:')
    folder_name = input('Введите название папки на ЯД, в которую хотите сохранить фотографии(Если нет папки просто нажмите Enter):')
    vk_token = input('Введите ключ VK API:')
    pi = PhotoInfo(token=vk_token)
    other = OtherLogic()
    yu = YaUploader(token=ya_token)
    yu.create_folder(folder_name=folder_name)
    pprint(pi.photo_info(user_id=user_id))
    other.photo_selection()
    pprint(yu.photo_uploader(folder_name = folder_name, dict_for_upload=other.dict_for_upload))
    other.file_info()