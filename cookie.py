import time
import keyboard
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")


def click_on_cookie(num):
    Big_cookie = driver.find_element(By.ID, "bigCookie")
    for i in range(num):
        Big_cookie.click()

def game_setup():
    time.sleep(3)
    while (driver.find_element(By.ID, "langSelect-EN").is_displayed() == False):
        time.sleep(1)
    driver.find_element(By.ID, "langSelect-EN").click()
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "cc_btn.cc_btn_accept_all").click()


def class_list_clicker(driver, class_name):
    class_list = driver.find_elements(By.CLASS_NAME, class_name)
    for upgrade in class_list:
        upgrade.click()

def is_there_something_to_buy(driver):
    return len(driver.find_elements(By.CLASS_NAME, "product.enabled")) > 0 or len(driver.find_elements(By.CLASS_NAME, "upgrade.enabled")) > 0

game_setup()

# Game Loop
while True:
    while(is_there_something_to_buy(driver) == False):
        click_on_cookie(10)

    class_list_clicker(driver, "upgrade.enabled") # Buy any upgrades that are available
    class_list_clicker(driver, "product.enabled") # Buy any products that are available
 
    cookies_amount = driver.find_element(By.ID, "cookies").text.split()[0]
    print("Number of cookies:", cookies_amount)

    # Kill switch
    if keyboard.is_pressed("q"):
        break
