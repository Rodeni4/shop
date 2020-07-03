import time


link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    try:
        browser.get(link)
        time.sleep(30)
        browser.find_element_by_class_name("btn-add-to-basket")
        result = True
    except:
        result = False
    assert result == True, "Кнопка не найдена!"