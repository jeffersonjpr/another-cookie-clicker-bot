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

game_setup()

# Game Loop
while True:
    click_on_cookie(5)

    #TODO: buy_available_upgrades()

    #TODO: Add a smart way to find buildings enabled to buy
    cursor = driver.find_element(By.ID, "product0")
    cursor.click()

    grandma = driver.find_element(By.ID, "product1")
    grandma.click()

    # farm = driver.find_element(By.ID, "product2")
    # farm.click()



# Kill switch
    if keyboard.is_pressed("q"):
        break
