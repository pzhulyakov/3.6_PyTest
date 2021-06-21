import time


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    print('\n Starting browser.')
    time.sleep(5)
    button_with_text = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    button_save = button_with_text.text
    assert button_save, 'Button is not found.'

