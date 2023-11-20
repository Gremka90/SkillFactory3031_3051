import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'D:/chrome-win32/chrome.exe'
    chrome_options.add_argument('--kiosk')
    return chrome_options
