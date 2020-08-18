import os
import requests


class YaUploader:
    def __init__(self, file_path: str, token):
        self.token = token
        self.file_path = file_path
        self.dir_name = os.path.basename(self.file_path)
        self.headers = {'Authorization': 'OAuth ' + self.token}
        self.url = 'https://cloud-api.yandex.net:443/v1/disk'

    def _get_files_from_folder(self) -> list:
        """Метод получает список файлов из каталога по пути self.file_path и возвращает список файлов для дальнейшей работы"""
        file_list = os.listdir(self.file_path)
        return file_list

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        YaUploader.create_folder(self)

        file_list = self._get_files_from_folder()
        url = self.url + '/resources/upload'
        for file in file_list:
            params = {'path': self.dir_name + '/' + file}
            # получаем url для загрузки:
            get_upload_url = requests.get(url, headers=self.headers, params=params)
            if not str(get_upload_url.status_code).startswith('2'):
                print(get_upload_url.json().get('message'))
            else:
                upload_url = get_upload_url.json().get('href')

                with open(os.path.join(self.file_path, file), 'rb') as f:
                    files = {'file': f}
                    # загружаем файл по полученному url:
                    upload_file = requests.put(upload_url, headers=self.headers, files=files)
                    if not str(upload_file.status_code).startswith('2'):
                        print(upload_file.json().get('message'))
                    else:
                        print(f'файл {file} был успешно загружен в директорию {self.dir_name}')
        return

    def create_folder(self):
        """метод создает папку на яндекс.диске с таким же именем как и в self.file_path"""
        url = self.url + '/resources'
        params = {'path': self.dir_name}
        create_folder = requests.put(url, headers=self.headers, params=params)
        if not str(create_folder.status_code).startswith('2'):
            print(create_folder.json().get('message'))
        else:
            print(f'директория {self.dir_name} была успешно создана')
        return


if __name__ == '__main__':
    # тут должен быть токен. или стоило взять его из инпута?
    yandexOAuth = ''
    path = os.path.normpath(input('укажите путь к папке: '))
    if not os.path.exists(path):
        print(f'папки {path} не существует')
    else:
        uploader = YaUploader(path, yandexOAuth)
        uploader.upload()
