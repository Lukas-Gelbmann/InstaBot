from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time
import os

def main():
    driver = getdriver()
    getwebsite(driver)
    fetch(driver)

    
def getdriver():
    print('getdriver')
    driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
    return driver


def getwebsite(driver):
    print('getwebsite')
    driver.get('https://www.buzzfeed.com/chelseamarshall/best-dog-pictures')
    time.sleep(5)


def fetch(driver):
    print('fetch')
    driver.find_element_by_class_name('qc-cmp-button').click()
    time.sleep(2)
    for _ in range(55):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(0.3)
    x = 0

    programpath = os.path.dirname(__file__)
    path = os.path.join(programpath, 'pictures/')

    if not os.path.exists(path):
        os.makedirs(path)
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        print(image.get_attribute('src'))
        f = open(path + str(x), 'wb')
        f.write(urllib.request.urlopen(image.get_attribute('src')).read())
        f.close()
        if os.path.getsize(path + str(x)) < 1000:
            os.remove(path + str(x))
        x += 1



main()
