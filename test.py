import pytest
from selenium import webdriver
import time
import math


def test_basket_button_should_be_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed(), "Button isn't displayed"

