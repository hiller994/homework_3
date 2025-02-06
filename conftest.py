import pytest
from selene import browser, be, have

@pytest.fixture(scope='session')
def open_browser():
    browser.config.window_height = 480  # высота браузера
    browser.config.window_width = 640  # ширина браузера
    browser.open('https://duckduckgo.com/')
    yield
    browser.quit()