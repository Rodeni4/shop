import pytest
import time
from selenium import webdriver


@pytest.mark.parametrize('language', ["ru", "en-gb"])
# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("#login_link")
