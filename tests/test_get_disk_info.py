from src.data.main_data import MainData
from src.api_methods.get_methods import GetMethods



data = MainData()


def test_get_disk_info():
    url = f'{data.basic_url}{data.endpoints["files"]}'
    disk = GetMethods()

    assert disk.check_status_code(url) == 401,\
        "Код ответа не соответствует ожидаемому"

    disk.get_all_file_names()
