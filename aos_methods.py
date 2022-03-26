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
    sleep(3)

    if driver.current_url == locators.advantage_url and driver.title == locators.advantage_title:
       print(" ")
       print(f"Amazing! advantageonlineshopping website launched successfully")
       print(" ")
       print(f"AOS Home Page URL: {driver.current_url}\nHome Page Title: {driver.title}")
       sleep(2)
    else:
       print(f"AOS website didn't launch. Check your code or application!")
       print(f"Current URL: {driver.current_url}\nHome Page Title: {driver.title}")

def create_new_account():
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a[id="hrefUserIcon"]').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
    sleep(1)
    for data, value in locators.account_test_data.items():
        driver.find_element(By.XPATH, f'//input[@name="{data}"]').send_keys(value)
        sleep(1)

    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    driver.find_element(By.ID, 'menuUser')
    displayed_username = driver.find_element(By.CSS_SELECTOR, 'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    print(" ")
    print(f'New User with username: {locators.user_name}, and password: {locators.password} created!')
    print(" ")

def sign_out():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.5)
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        print(" ")
        print(f'Logout Successful! at {datetime.datetime.now()}')
        print(" ")

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
    sleep(0.5)
    driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').click()
    sleep(0.5)
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
    sleep(1)
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
    sleep(1)
    driver.find_element(By.NAME, 'follow_twitter').click()
    sleep(1)
    driver.find_element(By.NAME, 'follow_linkedin').click()
    driver.get("https://advantageonlineshopping.com/#/")
    parent_window = driver.current_window_handle
    print(" ")
    print("Parent window handle", parent_window)
    print(" ")
    child_windows=driver.window_handles
    print(" ")
    print("Type of all windows", type(child_windows))
    print(" ")
    for child in child_windows:
        print(" ")
        print(child)
        if parent_window!= child:
            print(" ")
            print("Switching to new window/tab")
            driver.switch_to.window(child)
            print(" ")
            print("title is ",driver.title)
            driver.close()
            driver.switch_to.window(parent_window)
            assert driver.current_url == locators.advantage_url
            sleep(2)
    driver.switch_to.window(parent_window)
    print(" ")
    print("Follow us links validated successfully")
    print(" ")

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
    sleep(1)
    print(" ")
    print(f'Successfully login with New user : {locators.user_name}, and password: {locators.password} !')
    print(" ")

def delete_user():
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//div/label[contains(.,"No orders")]').is_displayed()
    sleep(0.5)
    print(" ")
    print(f'No Orders Displayed ')
    print(" ")
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.user_name}")]').is_displayed()
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "deletePopupBtn").click()
    print(" ")
    print(f'Account has been deleted.')
    print(" ")
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    driver.find_element(By.ID, 'signInResultMessage').is_displayed()
    print(" ")
    print(f'Incorrect user name or password.')
    print(" ")


def tear_Down():

    if driver is not None:
        print(" ")
        print(f"The test is completed successfully, Amazing!!")
        driver.close()
        driver.quit()

