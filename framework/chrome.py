from framework.browser import Browser
from framework.configmanager import ConfigManager
from selenium import webdriver

class Chrome(Browser):
    def __init__(self):
        super().__init__()

        if not self.driver:
            options = webdriver.ChromeOptions()
            options.page_load_strategy = ConfigManager.get_json_data("browser", "load_strategy")
            options.add_argument(ConfigManager.get_json_data("browser", "language_browser"))
            options.add_argument(ConfigManager.get_json_data("browser", "operating_mode"))
            options.add_argument(ConfigManager.get_json_data("browser", "screen size"))
            self.driver = webdriver.Chrome(options)
    
    def __del__(self):
        self.driver.quit()
        print("Очистка экземпляров")