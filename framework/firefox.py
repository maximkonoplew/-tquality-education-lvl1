from framework.browser import Browser
from configmanager import ConfigManager
from selenium import webdriver

class Firefox(Browser):
    def __init__(self):
        super().__init__()

    def create_driver(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = ConfigManager.get_json_data("browser", "load_strategy")
        options.add_argument(ConfigManager.get_json_data("browser", "language_browser"))
        options.add_argument(ConfigManager.get_json_data("browser", "operating_mode"))
        driver = webdriver.Firefox(options)
        return driver

driver = Firefox().create_driver()
driver.get(ConfigManager.get_json_data("browser", "start_url"))