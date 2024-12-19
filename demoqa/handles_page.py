from framework.base_form import Base_form
from demoqa.button import Button
from demoqa.text import Text
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from loguru import logger

class Handles_page(Base_form):
    __BUTTON_BROWSER_WINDOWS_LEFT_PANNEL = Button((By.XPATH, "//span[contains(text(), 'Browser Windows')]"), 'Browser Windows')
    __TITLE = Text((By.XPATH, "//*[@class='text-center']"), "Browser Windows")
    __BUTTON_NEW_TAB = Button((By.XPATH, "//button[@id='tabButton']"), "tabButton")
    __BUTTON_ELEMENTS_LEFT_PANNEL = Button((By.XPATH, "//div[@class='header-wrapper']/child::div[contains(text(), 'Elements')]"), 'Elements')
    __BUTTON_LINKS = Button((By.XPATH, "//li[@id='item-5']/child::span[contains(text(), 'Links')]"), 'Links')
    __BUTTON_HOME = Button((By.XPATH, "//a[@id='simpleLink']"), "simpleLink")

    
    def __init__(self, locator, name):
        super().__init__(locator, name)
    
    def go_to_browser_windows(self):
        logger.info("2. На открывшейся странице в левом меню кликнуть пункт Browser Windows")
        self.__BUTTON_BROWSER_WINDOWS_LEFT_PANNEL.find_click_element()
        return self.__TITLE.wait_element()
    
    def create_another_tab(self):
        logger.info("3. Кликнуть на кнопку New Tab")
        self.__BUTTON_NEW_TAB.find_click_element()  

    def go_to_links(self):
        logger.info("5. В левом меню выбрать Elements → Links")
        self.__BUTTON_ELEMENTS_LEFT_PANNEL.find_click_element()

        button_link = self.__BUTTON_LINKS.find_element()
        actions = ActionChains(self.driver)
        actions.move_to_element(button_link)
        actions.click(button_link)
        actions.perform()
        
        return self.__TITLE.wait_element()
    
    def go_to_main_page(self):
        logger.info("6. Перейти по ссылке Home")
        self.__BUTTON_HOME.find_click_element()