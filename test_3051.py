
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_pets_1(selenium):
    selenium.binary_location = 'D:/chrome-win32/chrome.exe'
    selenium.get('http://petfriends.skillfactory.ru/login')
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.fullscreen_window()
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[style="max-width: 100px; max-height: 100px;"]')))
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table > tbody > tr > td')))


def test_pets_2(selenium):
    selenium.binary_location = 'D:/chrome-win32/chrome.exe'
    selenium.get('http://petfriends.skillfactory.ru/login')
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.fullscreen_window()
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    selenium.implicitly_wait(10)
    selenium.find_element(By.CSS_SELECTOR, 'table[class = "table table-hover"]')

