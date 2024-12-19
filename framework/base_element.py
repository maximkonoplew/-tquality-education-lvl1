from framework.chrome import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.configmanager import ConfigManager

class Base_element:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.driver = Chrome().driver

    def find_element(self):
        return self.driver.find_element(*self.locator)
    
    def find_elements(self):
        return self.driver.find_elements(*self.locator)
    
    def wait_element(self):
        time_out = ConfigManager.get_json_data("wait", "time_out")
        return WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(self.locator))