import pytest
from selenium import webdriver
import time
import math
from selenium.common.exceptions import NoSuchElementException


def test_basket_button_should_be_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        element_is_displayed = browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed()
    except NoSuchElementException:
        element_is_displayed = False
    assert element_is_displayed, "Element isn't displayed or not found"

