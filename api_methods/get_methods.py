from api_methods.basic_methods import BasicMethods
from src.main_data import MainData
import requests


class GetMethods(BasicMethods):

    def get_all_file_names(self):
        response = requests.get(url=f'{MainData.basic_url}{MainData.endpoints["files"]}',
                                headers={'Authorization': f'OAuth {MainData.oauth_token}'})
        r = response.json()

        print('\nСписок доступных файлов и папок:')
        # Заходим внутрь списка 'items' и находим ключ 'path'
        for item in r.get('items'):
            path = item.get('path')
            beautified_path = path.replace('disk:/', '')  # Убираем название корневой директории "для красоты"
            print(beautified_path)