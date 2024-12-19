from selenium import webdriver
from selenium.webdriver.common.by import By
import json

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
            __options = webdriver.ChromeOptions()
            __options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            __options.add_argument("--incognito")
            self.__driver = webdriver.Chrome(options=__options)

    def get_driver(self):
        return self.__driver
    
    def close_driver(self):
        self.__driver.quit()


class Home_page:
    __locator_about = "//div[@class='supernav_container']/descendant::a[@class='menuitem ' and contains(text(), 'About')]"
    
    @classmethod
    def get_page_home(cls, driver):
        with open('config.json', 'r') as file:
            url = json.load(file)["url_home_page"]
        (driver.get_driver()).get(url)
        return True
    
    @classmethod
    def get_about(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_about).click()
        return True
    
class Player_page:
    __locator_gamers_online = "//div[@class='online_stat_label gamers_online']/ancestor::div[@class='online_stat']"
    __locator_gamers_in_game = "//div[@class='online_stat_label gamers_in_game']/ancestor::div[@class='online_stat']"
    __locator_home_page = "//div[@aria-label='Global Menu']/a[@data-tooltip-content='.submenu_Store']"

    @classmethod
    def player_comparison(cls, driver):
        player_in_online =  (driver.get_driver()).find_element(By.XPATH, cls.__locator_gamers_online)
        player_in_game = (driver.get_driver()).find_element(By.XPATH, cls.__locator_gamers_in_game)
        return int(player_in_online.text[6::].replace(',', '')) > int(player_in_game.text[11::].replace(',', ''))
    
    @classmethod
    def get_back_page_home(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_home_page).click()
        return True
