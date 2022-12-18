import requests
from pprint import pprint
import os

# 2 задание

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    # Функция для получения URL загрузки..
    def get_upload_url(self, file_path_on_disk):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {'path': file_path_on_disk}
        resp = requests.get(upload_url, params=params, headers=headers)
        return resp.json()

    # Функция для удаления существующего пути (чтобы программа успешно сработала)..
    def delete_folder(self, folder_name):
        self.folder_name = folder_name
        params = {'path': folder_name}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        resp = requests.delete(url, params=params, headers=headers)
        return resp.json()

    # Функция для создания новой папки для загружаемых с компьютера файлов..
    def create_folder(self, folder_name):
        self.folder_name = folder_name
        params = {'path': folder_name}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        resp = requests.put(url, params=params, headers=headers)
        return resp.json()

    # Функция для загрузки файлов в папку на Яндекс.Диск..
    def upload_file_on_disk(self, path_to_file):
        for filename in list(os.listdir(os.path.join(os.getcwd(), path_to_file))):
            self.path_to_file = path_to_file
            result = self.get_upload_url(file_path_on_disk=f'Avatars/{filename}')
            href = result.get("href", "")
            resp = requests.put(href, data=open(os.path.join(path_to_file, filename), 'rb'))
            if resp.status_code == 201:
                print('Success')

if __name__ == '__main__':
    path_to_files = 'C:\Milkbusiness\Codes\myPractice\HTTP\Files'
    token = ''
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    folder_name = 'Avatars'
    uploader = YaUploader(token)
    pprint(uploader.delete_folder(folder_name))
    pprint(uploader.create_folder(folder_name))
    result = uploader.upload_file_on_disk(path_to_files)
    
   
    


