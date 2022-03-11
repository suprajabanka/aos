import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import aos_locators as locators
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='c:\\Users\\ramak\\PycharmProjects\\pythonProject\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setup():
    print(f'launch {locators.website} Home Page')

driver.maximize_window()
driver.implicitly_wait(30)


driver.get('https://advantageonlineshopping.com/#/')
sleep(2)

if driver.current_url == locators.advantage_url and driver.title == locators.advantage_title:
   print(f"Amazing! advantageonlineshopping website launched successfully")
   print(f"AOS Home Page URL: {driver.current_url}\nHome Page Title: {driver.title}")
   sleep(2)
else:
   print(f"AOS website didn't launch. Check your code or application!")
   print(f"Current URL: {driver.current_url}\nHome Page Title: {driver.title}")

def create_new_user():
    print(' ------------- New user Creation ----------------')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a[id="hrefUserIcon"]').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
    sleep(3)
    for data, value in locators.account_test_data.items():
        driver.find_element(By.XPATH, f'//input[@name="{data}"]').send_keys(value)
        sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    print(f'New User with username: {locators.username}, and password: {locators.password} was created!')

def validate_new_user_is_created(new_username):
    print('--------- Validate New User is Created ------------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR, 'span[data-ng-show="userCookie.response"]'
                                                              '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    if new_username == displayed_username:
        print(f'New user is created')
        print(f'New user username: {new_username}, new username displayed: {displayed_username}')
    else:
        print('New user was not created')

def log_out():
    print(' --------Log out--------------- ')
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, locators.username).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    print(f'Logout Successful! at {datetime.datetime.now()}')

def log_in(new_username, new_password):
    print('---- Login with new user --------')
    sleep(1)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.25)
    print('Successfully logged in')

def validate_new_user_can_login(new_username):
    print(' --------- Validate New user is Created-----------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR, 'span[data-ng-show="userCookie.response"]'
                                                              '[class="hi-user containMiniTitle ng-binding"]').get_attribute(
        'innerText')

    if new_username == displayed_username:
        print('New user is created and displayed')
        print(f'New user username: {new_username}, new user displayed on the page: {displayed_username}')
    else:
        print('New user was not logged in!')

def tear_down():

    if driver is not None:
        print(f"The test is completed")
        driver.close()
        driver.quit()




#setup()
#create_new_user()
#validate_new_user_is_created(locators.username)
#log_out()
#log_in(locators.username, locators.password)
#validate_new_user_can_login(locators.username)
#log_out()
#tear_down()