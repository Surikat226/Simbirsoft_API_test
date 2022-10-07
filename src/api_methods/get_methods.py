from src.api_methods.basic_methods import BasicMethods, logger
from src.data.main_data import MainData
import requests

data = MainData()


class GetMethods(BasicMethods):

    def get_all_file_names(self):
        response = requests.get(url=f'{data.basic_url}{data.endpoints["files"]}',
                                headers={'Authorization': f'OAuth {data.oauth_token}'})
        r = response.json()

        logger.info('\nСписок доступных файлов и папок:')
        # Заходим внутрь списка 'items' и находим ключ 'path'
        for item in r.get('items'):
            path = item.get('path')
            beautified_path = path.replace('disk:/', '')  # Убираем название корневой директории "для красоты"
            logger.info(beautified_path)