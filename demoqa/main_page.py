from framework.base_form import Base_form
from demoqa.button import Button
from selenium.webdriver.common.by import By
from framework.chrome import Chrome
from loguru import logger


class Main_page(Base_form):
    __BUTTON_ALERTS_FRAMES_WINDOWS = Button((By.XPATH, "//*[contains(text(), 'Alerts, Frame & Windows')]"), "Button Alerts Frame Windows")
    __BUTTON_ELEMENTS = Button((By.XPATH, "// div[@class='card mt-4 top-card']/descendant::* [contains(text(), 'Elements')]"), "Elements")
    
    def __init__(self, locator, name):
        super().__init__(locator, name)
    
    def go_to_alerts_frames_windows(self):
        logger.info("2. Кликнуть на кнопку Alerts, Frame & Windows")
        self.__BUTTON_ALERTS_FRAMES_WINDOWS.find_click_element()
    
    def go_to_elements(self):
        logger.info("2. Кликнуть на кнопку Elements")
        self.__BUTTON_ELEMENTS.find_click_element()

    def clear_instance(self):
        Chrome().__del__()