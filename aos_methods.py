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

def setUp():
    print(f'launch {locators.website} Home Page')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://advantageonlineshopping.com/#/')
    sleep(10)

    if driver.current_url == locators.advantage_url and driver.title == locators.advantage_title:
       print(f"Amazing! advantageonlineshopping website launched successfully")
       print(f"AOS Home Page URL: {driver.current_url}\nHome Page Title: {driver.title}")
       sleep(10)
    else:
       print(f"AOS website didn't launch. Check your code or application!")
       print(f"Current URL: {driver.current_url}\nHome Page Title: {driver.title}")

def create_new_account():
    sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'a[id="hrefUserIcon"]').click()
    sleep(5)
    driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
    sleep(3)
    for data, value in locators.account_test_data.items():
        driver.find_element(By.XPATH, f'//input[@name="{data}"]').send_keys(value)
        sleep(1)

    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    driver.find_element(By.ID, 'menuUser')
    displayed_username = driver.find_element(By.CSS_SELECTOR, 'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')

def sign_out():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        print(f'Logout Successful! at {datetime.datetime.now()}')

def validate_homepage_texts():
    driver.get('https://advantageonlineshopping.com/#/')
    assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    assert driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed()
    print(' ')
    print("speakers, tablets, laptops, mice, headphones and Main logo is displayed properly")
    print(' ')
    driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').click()
    driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').click()
    driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').click()
    print(' ')
    print("Top navigation menu items are clickable")
    print(' ')

def validate_contact_us():
    sleep(1)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(1)
    sleep(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(2)
    assert driver.find_element(By.ID, 'send_btnundefined').is_enabled()
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,
                               '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    sleep(1)
    print('')
    print('CONTACT US Form validated successfully!')
    print('')

def validate_follow_us_links():
    driver.find_element(By.NAME, 'follow_facebook' ).click()
    sleep(2)
    driver.find_element(By.NAME, 'follow_twitter').click()
    sleep(2)
    driver.find_element(By.NAME, 'follow_linkedin').click()
    print("Follow us links validated successfully")
    parent_page = driver.current_window_handle
    sleep(3)
    for handle in driver.window_handles:
        if handle!= parent_page:
            driver.switch_to.window(parent_page)
            assert driver.current_url == locators.advantage_url
            sleep(2)


def log_in():
    print('---- Login with new user --------')
    sleep(1)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.25)
    print('Successfully logged in')

def delete_user():
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//div/label[contains(.,"No orders")]').is_displayed()
    sleep(0.25)
    print(f'No Orders Displayed ')
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.user_name}")]').is_displayed()
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
    print(f'Account has been deleted.')
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    driver.find_element(By.ID, 'signInResultMessage').is_displayed()
    print(f'Incorrect user name or password.')



def tear_Down():

    if driver is not None:
        print(f"The test is completed")
        driver.close()
        driver.quit()



