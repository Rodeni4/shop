

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    try:
        browser.get(link)
        browser.find_element_by_class_name("btn-add-t-basket")
        result = True
    except:
        result = False
    assert result == True, "кнопка не найдена"