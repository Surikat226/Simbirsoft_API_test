# Это простой проект по автоматизации тестирования API Яндекс.Диска.
В проекте реализован 1 скрипт, который
авторизуется в аккаунте Яндекс пользователя через API, получает список файлов и директорий на его Яндекс.Диске
и проверяет код ответа сервера на соответствие ожидаемому коду.  
Проект реализован по паттерну *PageObject*.

# Запуск тестов
- Желательно запускать тесты командой `pytest -s -v .\main.py`
- Логи тестов сохраняются в папку logs