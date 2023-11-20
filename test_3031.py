import time
from selenium.webdriver.common.by import By


def test_all_pets_present(selenium):
    selenium.get('http://petfriends.skillfactory.ru/login')
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.implicitly_wait(1)
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    selenium.implicitly_wait(1)
    text = selenium.find_element(By.CSS_SELECTOR, 'div[class =".col-sm-4 left"]').text
    number_of_pet = int((text.split('\n'))[1].replace('Питомцев: ', ''))
    tr = selenium.find_elements(By.CSS_SELECTOR, 'tr')
    assert number_of_pet == len(tr) - 1


def test_show_my_pets(selenium):
    selenium.get('http://petfriends.skillfactory.ru/login')
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    time.sleep(1)
    text = selenium.find_element(By.CSS_SELECTOR, 'div[class =".col-sm-4 left"]').text
    number_of_pet = int((text.split('\n'))[1].replace('Питомцев: ', ''))
    th = selenium.find_elements(By.CSS_SELECTOR, 'th[scope="row"]')
    photo_pets = 0
    for item in th:
        if item.find_element(By.CSS_SELECTOR, 'img').get_attribute('src'):
            photo_pets += 1
    assert photo_pets > float(number_of_pet / 2)



def test_have_name_age_breed(selenium):
    selenium.get('http://petfriends.skillfactory.ru/login')
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    time.sleep(1)
    text = selenium.find_element(By.CSS_SELECTOR, 'div[class =".col-sm-4 left"]').text
    number_of_pet = int((text.split('\n'))[1].replace('Питомцев: ', ''))
    th = selenium.find_elements(By.CSS_SELECTOR, 'tbody')
    pet_attribut = 0
    for item in th:
        for js in item.find_elements(By.CSS_SELECTOR, 'td'):
            if len(js.text) != 0:
                pet_attribut += 1
    assert number_of_pet*4 == pet_attribut


def test_uniq_name(selenium):
    selenium.get('http://petfriends.skillfactory.ru/login')
    time.sleep(1)
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.fullscreen_window()
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    time.sleep(1)
    th = selenium.find_element(By.CSS_SELECTOR, 'tbody').find_elements(By.CSS_SELECTOR, 'tr')
    names = []
    for item in th:
        for js in item.find_elements(By.CSS_SELECTOR, 'td')[:-3]:
            names.append(js.text)
    names_uniq = set(names)
    assert len(names_uniq) == len(names)

def test_uniq_pet(selenium):
    selenium.implicitly_wait(10)
    selenium.get('http://petfriends.skillfactory.ru/login')
    time.sleep(1)
    selenium.find_element(By.ID, 'email').send_keys('gremka901@gmail.com')
    selenium.find_element(By.ID, 'pass').send_keys('123')
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.fullscreen_window()
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
    time.sleep(1)
    th = selenium.find_element(By.CSS_SELECTOR, 'tbody').find_elements(By.CSS_SELECTOR, 'tr')
    attribute = []

    for item in th:
        for js in item.find_elements(By.CSS_SELECTOR, 'td')[:-1]:
            attribute.append(js.text)
    flag = 0
    data_pet = ''
    pet = []
    for i in attribute:
        data_pet += i
        flag += 1
        if flag == 3:
            pet.append(data_pet)
            data_pet = ''
            flag = 0
    uniq_pet = set(pet)
    assert len(uniq_pet) == len(pet)
