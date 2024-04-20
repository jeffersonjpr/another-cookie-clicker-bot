import time
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CookieBot:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.cookie_amount = 0

        self.__big_cookie = None

    def __get_big_cookie(self):
        if self.__big_cookie == None:
            self.__big_cookie = self.driver.find_element(By.ID, "bigCookie")
        return self.__big_cookie

    def click_on_cookie(self, num: int):
        for i in range(num):
            self.__get_big_cookie().click()

    def game_setup(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cc_btn.cc_btn_accept_all")))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cc_btn.cc_btn_accept_all"))).click()
        self.__big_cookie = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))


    def __class_list_clicker(self, class_name: str, invert=False):
        class_list = self.driver.find_elements(By.CLASS_NAME, class_name)

        if invert:
            class_list = class_list[::-1]

        for upgrade in class_list:
            upgrade.click()

    def is_there_something_to_do(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "product.enabled")) > 0 or len(self.driver.find_elements(By.CLASS_NAME, "upgrade.enabled")) > 0

    def get_cookie_amount(self):
        self.cookie_amount = self.driver.find_element(
            By.ID, "cookies").text.split()[0]
        return self.cookie_amount

    def buy_available_upgrades(self):
        self.__class_list_clicker("upgrade.enabled")

    def buy_available_products(self):
        self.__class_list_clicker("product.enabled", invert=True)

    def save_game(self, file_name="cookie_save.txt"):
        self.__click_options_button()

        self.__click_options_menu("Export save")

        with open(file_name, "w") as file:
            file.write(self.driver.find_element(By.ID, "textareaPrompt").text)
        
        self.driver.find_element(By.ID, "promptOption0").click()

        self.__click_options_button()
        # print save time
        print("Game saved: " + time.strftime("%H:%M:%S"))

    def __load_save_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                save = file.read()
        except FileNotFoundError:
            print("No save data found")
            return None

        if save == "":
            print("No save data found")
            return None
        
        return save
        
    def load_game(self, file_name="cookie_save.txt"):
        save = self.__load_save_file(file_name)
        
        if save == None:
            return
        
        self.__click_options_button()

        self.__click_options_menu("Import save")

        self.driver.find_element(By.ID, "textareaPrompt").send_keys(save)

        self.driver.find_element(By.ID, "promptOption0").click()

        self.__click_options_button()
        # print load time
        print("Game loaded: " + time.strftime("%H:%M:%S"))

    def __click_options_menu(self, select_option):
        list_buttons = self.driver.find_elements(By.CLASS_NAME, "option.smallFancyButton")
        for button in list_buttons:
            if button.text == select_option:
                button.click()
                break

    def __click_options_button(self):
        self.driver.find_element(By.ID, "prefsButton").click()