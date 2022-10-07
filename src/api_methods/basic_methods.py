# В условии задания не было ничего сказано про написание проверок кода ответа, но я решил дополнительно
# сделать её и вынести в базовый класс, чтобы наглядней показать, как я обычно пишу код по POM
import requests
from loguru import logger


logger.add('logs/test_logs.txt', format='{time} {level} {message}', level='INFO')


class BasicMethods:

    def check_status_code(self, url):
        request = requests.get(url)
        logger.info(f'\nКод ответа по адресу {url}: {request.status_code}')
        return request.status_code
