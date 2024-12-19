import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    __locator_menu = "//a[@class='pulldown_desktop' and contains(text(), 'New & Noteworthy')]"
    __popup_menu_item = "//a[@class='popup_menu_item' and contains(text(), 'Top Sellers')]"
    
    @classmethod
    def get_page_home(cls, driver):
        with open('config.json', 'r') as file:
            __url = json.load(file)["url_home_page"]
        (driver.get_driver()).get(__url)
        return True
    
    @classmethod
    def get_menu(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_menu).click()
        WebDriverWait((driver.get_driver()), 10).until(EC.visibility_of_element_located((By.XPATH, cls.__popup_menu_item))).click()
        return True

class Games_page:
    __locator_button = "//button[@class = 'DialogButton _DialogLayout Primary Focusable']"
    __locator_steam_linux = "//span[contains(text(), 'SteamOS + Linux')]/preceding-sibling::span"
    __locator_narrow_by_number_of_players = "//div[contains(text(), 'Narrow by number of players')]"
    __locator_lan_co_op = "//span[contains(text(), 'LAN Co-op')]/preceding-sibling::span"
    __locator_tag_suggest = "//*[@id='TagSuggest']"
    __locator_tab_filter_control_count = "//div[@data-loc='Action']/descendant::span[@class='tab_filter_control_count']"
    __locator_tab_action_checkbox = "//div[@data-loc='Action']/descendant::span[@class='tab_filter_control_checkbox']"
    __list_of_games = "//div[@class='search_results_count']"
    __locator_name_game = "//div[@id='search_resultsRows']/a[1]/descendant::span[@class='title']"
    __locator_date_game = "//div[@id='search_resultsRows']/a[1]/descendant::div[@class='col search_released responsive_secondrow']"
    __locator_price_game = "//div[@id='search_resultsRows']/a[1]/descendant::div[@class='discount_final_price']"
    __locator_page_first_game = "//div[@id='search_resultsRows']/a[1]"

    @classmethod
    def get_scroll(cls, driver):
        with open('config.json', 'r') as file:
            window_scroll = json.load(file)["window"]
        (driver.get_driver()).execute_script(window_scroll)
        WebDriverWait((driver.get_driver()), 10).until(EC.visibility_of_element_located((By.XPATH, cls.__locator_button))).click()
        return True
    
    @classmethod
    def get_steam_lunux(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_steam_linux).click()
        return True
    
    @classmethod
    def get_LAN(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_narrow_by_number_of_players).click()
        time.sleep(1)
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_lan_co_op).click()
        return True

    @classmethod
    def get_action(cls, driver):
        with open('config.json', 'r') as file:
            game_genre = json.load(file)["game genre"]
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_tag_suggest).send_keys(game_genre)
        time.sleep(1)
        value_game = (driver.get_driver()).find_element(By.XPATH,  cls.__locator_tab_filter_control_count).text
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_tab_action_checkbox).click()
        time.sleep(1)
        value_game_in_list = (driver.get_driver()).find_element(By.XPATH, cls.__list_of_games).text
        return int(value_game) == int(value_game_in_list[:2])
    
    @classmethod
    def get_data_first_game(cls, driver):
        name = (driver.get_driver()).find_element(By.XPATH, cls.__locator_name_game).text
        date = (driver.get_driver()).find_element(By.XPATH, cls.__locator_date_game).text
        time.sleep(1)
        price = (driver.get_driver()).find_element(By.XPATH, cls.__locator_price_game).text
        return name, date, price
    
    @classmethod
    def get_page_first_game(cls, driver):
        (driver.get_driver()).find_element(By.XPATH, cls.__locator_page_first_game).click()
        return True

class First_game_page:
    __locator_name_game_in_page = "//div[@id = 'appHubAppName']"
    __locator_date_game_in_page = "//div[@class='date']"
    __locator_price_game_in_page = "//div[@class='leftcol game_description_column']/descendant::div[@class='discount_final_price'][1]"

    @classmethod
    def get_data_first_game_in_page(cls, driver):
        name_on_page = (driver.get_driver()).find_element(By.XPATH, cls.__locator_name_game_in_page).text
        date_one_page = (driver.get_driver()).find_element(By.XPATH, cls.__locator_date_game_in_page).text
        price_on_page = ((driver.get_driver()).find_element(By.XPATH, cls.__locator_price_game_in_page).text)[:-1]
        return name_on_page, date_one_page, price_on_page
