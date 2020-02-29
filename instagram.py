from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from random import seed
from random import randint
import os

# seed random number generator

email = 'owexactly00@protonmail.com'
password = 'mM9cjG9EpZaATis'
name = 'bestdogpictures2020'
image_path = os.path.dirname(__file__) + '/pics/test.jpeg'
followsize = 30
unfollowsize = 30


def main():
    seed(1)
    driver = getdriver()
    getwebsite(driver)
    login(driver)
    #follow(driver)
    #unfollow(driver)
    #addpicture(driver)


def getdriver():
    print('getdriver')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36")
    driver = webdriver.Firefox(profile, executable_path='/usr/bin/geckodriver')
    return driver


def getwebsite(driver):
    print('getwebsite')
    driver.get('https://www.instagram.com/accounts/login')
    time.sleep(5)


def login(driver):
    print('login')
    emailInput = driver.find_elements_by_css_selector('form input')[0]
    passwordInput = driver.find_elements_by_css_selector('form input')[1]
    emailInput.send_keys(email)
    passwordInput.send_keys(password)
    time.sleep(2)
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(5)
    buttons = driver.find_elements_by_css_selector('button')
    buttons[1].click()
    time.sleep(2)


def follow(driver):
    print('follow')
    driver.get('https://www.instagram.com/explore/people/suggested/')
    time.sleep(5)
    followed = 0
    for index in range(1000):
        followbuttons = driver.find_elements_by_css_selector('button')
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, window.scrollY + 55)")
        if randint(0, 3) == 0:
            followed += 1
            time.sleep(randint(1, 3))
            followbuttons[index].click()
            if followed == followsize:
                return




def unfollow(driver):
    print('unfollow')
    driver.get('https://www.instagram.com/' + name + '/')
    time.sleep(5)
    buttons = driver.find_elements_by_class_name('-nal3')
    buttons[2].click()
    time.sleep(3)

    unfollowbuttons = driver.find_elements_by_css_selector('button')
    for x in range(unfollowsize):
        unfollowbuttons[x].click()
        time.sleep(1)
        driver.find_element_by_class_name('aOOlW -Cab').click()
        time.sleep(1)


def addpicture(driver):
    print('addpicture')
    add = driver.find_element_by_class_name('_8-yf5')
    driver.execute_script('el = document.elementFromPoint(580, 820); el.click();')

    elm = driver.find_element_by_xpath("//input[@type='file']")
    time.sleep(5)
    elm.send_keys(image_path)




main()
