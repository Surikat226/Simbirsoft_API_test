from src.main_data import MainData
from api_methods.get_methods import GetMethods


def test_get_disk_info():
    url = f'{MainData.basic_url}{MainData.endpoints["files"]}'
    disk = GetMethods()

    assert disk.check_status_code(url) == 401,\
        "Код ответа не соответствует ожидаемому"

    disk.get_all_file_names()
