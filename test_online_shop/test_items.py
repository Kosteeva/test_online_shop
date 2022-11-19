from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_guest_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert "successful" not in button.text
