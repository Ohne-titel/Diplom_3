import pytest
from selenium import webdriver
from urls import URL


# @pytest.fixture(params=['firefox', 'chrome'])
# def driver(request):
#     if request.param == 'firefox':
#         driver = webdriver.Firefox()
#         driver.maximize_window()
#     elif request.param == 'chrome':
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#     driver.get(URL)
#
#     yield driver
#
#     driver.quit()

@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(URL)

    yield chrome

    chrome.quit()
