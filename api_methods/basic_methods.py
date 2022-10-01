# В условии задания не было ничего сказано про написание проверок кода ответа, но я решил дополнительно
# сделать её и вынести в базовый класс, чтобы наглядней показать, как я обычно пишу код по POM
import requests


class BasicMethods:

    def check_status_code(self, url):
        request = requests.get(url)
        print(f'\nКод ответа по адресу {url}: {request.status_code}')
        return request.status_code