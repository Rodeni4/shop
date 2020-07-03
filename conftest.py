import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Сначала добавляем обработчик опции в функции pytest_addoption
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ...(etc.)")
@pytest.fixture
def browser(request):
    # Добавим логику обработки командной строки. Для запроса значения параметра
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()



