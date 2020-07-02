import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Сначала добавляем обработчик опции в функции pytest_addoption
def pytest_addoption(parser):
    #Можно задать значение параметра по умолчанию, default="chrome"
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ...(etc.)")

# если добавить (scope="module") браузер запустится и закроется один раз
@pytest.fixture
def browser(request):
    print("\nЗапускается браузер для тестирования..")
    #browser = webdriver.Chrome()
    #return browser

    #Добавим логику обработки командной строки. Для запроса значения параметра
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
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


