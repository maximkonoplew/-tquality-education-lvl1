from framework.base_form import Base_form
from demoqa.button import Button
from demoqa.text import Text
from demoqa.table import table
from selenium.webdriver.common.by import By
from loguru import logger

class Table_page(Base_form):
    __BUTTON_TABLES_LEFT_PANNEL = Button((By.XPATH, "//span[contains(text(), 'Tables')]"), 'Button Tables')
    __TITLE = Text((By.XPATH, "//*[@class='text-center']"), "Title Tables")
    __ADD_NEW_RECORD_BUTTON = Button((By.XPATH, "//button[@id='addNewRecordButton']"), "addNewRecordButton")
    __REGISTRATION_FORM = Text((By.XPATH, "//div[@id='registration-form-modal']"), "Registration Form")
    __BUTTON_SUBMIT = Button((By.XPATH, "//button[@id = 'submit']"), "submit")
    __ELEMENT_TO_CHECK_FIRST_USER = Text((By.XPATH, "//div[contains(text(), 'Jon')]"),  "name_user1")
    __ELEMENT_TO_CHECK_SECOND_USER = Text((By.XPATH, "//div[contains(text(), 'Ben')]"),  "name_user2")
    __BUTTON_DELETE_FIRST_USER = Button((By.XPATH, "//span[@id ='delete-record-4']"), "delete_user_1")
    
    def __init__(self, locator, name):
        super().__init__(locator, name)
    
    def go_to_web_tables(self):
        logger.info("2. На открывшейся странице в левом меню кликнуть пункт Web Tables")
        self.__BUTTON_TABLES_LEFT_PANNEL.find_click_element()
        return self.__TITLE.wait_element()

    def add_new_user(self, number_user, args):
        
        logger.info("3. Кликнуть на кнопку Add")
        self.__ADD_NEW_RECORD_BUTTON.find_click_element()
        table(args).create_user()
        self.__BUTTON_SUBMIT.find_click_element()
        if number_user == 1:
            logger.info("4. Ввести данные пользователя User 1 из таблицы и затем нажать на кнопку Submit")
            assert self.__ELEMENT_TO_CHECK_FIRST_USER.find_element().text == args[0]
        elif number_user == 2:
            logger.info("4. Ввести данные пользователя User 1 из таблицы и затем нажать на кнопку Submit")
            assert self.__ELEMENT_TO_CHECK_SECOND_USER.find_element().text == args[0]

    def delete_first_user(self):
        logger.info("5. Нажать на кнопку Delete в строке пользователя User 1")
        self.__BUTTON_DELETE_FIRST_USER.find_click_element()
        assert len(self.__ELEMENT_TO_CHECK_FIRST_USER.find_elements()) == 0
    