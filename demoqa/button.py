from framework.base_element import Base_element

class Button(Base_element):

    def __init__(self, locator, name):
        super().__init__(locator, name)

    def find_click_element(self):
        element = self.find_element()
        element.click()