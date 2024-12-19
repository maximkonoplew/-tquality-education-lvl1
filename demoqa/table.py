from selenium.webdriver.common.by import By
from framework.chrome import Chrome

class table:
    __FIRST_NAME = "//input[@id = 'firstName']"
    __LAST_NAME = "//input[@id = 'lastName']"
    __USER_EMAIL = "//input[@id = 'userEmail']"
    __AGE = "//input[@id = 'age']"
    __SALARY = "//input[@id = 'salary']"
    __DEPARTMENT = "//input[@id = 'department']"

    def __init__(self, args):
        self.__USER_DATA = args
        self.driver = Chrome().driver

    def create_user(self):
        self.driver.find_element(By.XPATH, self.__FIRST_NAME).send_keys(f"{self.__USER_DATA[0]}")
        self.driver.find_element(By.XPATH, self.__LAST_NAME).send_keys(f"{self.__USER_DATA[1]}")
        self.driver.find_element(By.XPATH, self.__USER_EMAIL).send_keys(f"{self.__USER_DATA[2]}")
        self.driver.find_element(By.XPATH, self.__AGE).send_keys(f"{self.__USER_DATA[3]}")
        self.driver.find_element(By.XPATH, self.__SALARY).send_keys(f"{self.__USER_DATA[4]}")
        self.driver.find_element(By.XPATH, self.__DEPARTMENT).send_keys(f"{self.__USER_DATA[5]}")