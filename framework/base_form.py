from framework.chrome import Chrome

class Base_form:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.driver = Chrome().driver

    def find_element(self):
        return self.driver.find_element(*self.locator)