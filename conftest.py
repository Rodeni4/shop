import pytest
from selenium import webdriver

# если добавить (scope="module") браузер запустится и закроется один раз
@pytest.fixture
def browser():
    print("\nЗапускается браузер для тестирования..")
    browser = webdriver.Chrome()
    #return browser

    yield browser
    # этот код выполнится после завершения теста
    print("\nЗакрытие браузера..")
    browser.quit() \

# если добавить (autouse=True) фикстура запустится для каждого теста даже без явного вызова
@pytest.fixture
def prepare_data():
    print()
    print("Подготовка некоторых критических данных для каждого теста")


