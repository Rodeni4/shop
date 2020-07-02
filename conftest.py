import pytest
from selenium import webdriver


# Сначала добавляем обработчик опции в функции pytest_addoption
def pytest_addoption(parser):
    #Можно задать значение параметра по умолчанию, default="chrome"
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

# если добавить (scope="module") браузер запустится и закроется один раз
@pytest.fixture
def browser(request):
    print("\nЗапускается браузер для тестирования..")
    browser = webdriver.Chrome()
    #return browser

    #Добавим логику обработки командной строки. Для запроса значения параметра
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # этот код выполнится после завершения теста
    print("\nЗакрытие браузера..")
    browser.quit()

# если добавить (autouse=True) фикстура запустится для каждого теста даже без явного вызова
@pytest.fixture
def prepare_data():
    print()
    print("Подготовка некоторых критических данных для каждого теста")


