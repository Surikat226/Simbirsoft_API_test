class MainData:

    # Базовый урл, к которому в дальнейших тестах подставлялись бы эндпоинты
    basic_url = 'https://cloud-api.yandex.net/v1'

    # Токен авторизации
    oauth_token = 'y0_AgAAAABk_jZOAADLWwAAAADQMp672AEh71AgTx-j4Xdu2_e9RSURmU8'

    # Список эндпоинтов, который пополнялся бы в случае написания каких-то новых тестов
    endpoints = {
        'files': '/disk/resources/files'
    }
