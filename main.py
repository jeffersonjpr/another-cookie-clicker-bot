from selenium import webdriver
from cookie_bot import CookieBot
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_bot = CookieBot(driver)

cookie_bot.game_setup()
cookie_bot.load_game()

start_time = time.time()

# Game Loop
while True:
    while(not cookie_bot.is_there_something_to_do()):
        cookie_bot.click_on_cookie(10)

    # Buy any upgrades that are available
    cookie_bot.buy_available_upgrades()
    # Buy any products that are available
    cookie_bot.buy_available_products()
 
    print("Number of cookies:", cookie_bot.get_cookie_amount())

    # save game every 60 seconds
    if time.time() - start_time > 60:
        cookie_bot.save_game()
        start_time = time.time()
