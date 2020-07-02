# shop
3.6 PyTest - параметризация, конфигурирование, плагины

Запуск: pytest -s -v test_items.py

Conftest.py и передача параметров в командной строке:

pytest -s -v --browser_name=chrome test_items.py

pytest -s -v --browser_name=firefox test_items.py


Задание: запуск автотестов для разных языков интерфейса:

pytest -s -v --browser_name=chrome --language=en test_items.py

