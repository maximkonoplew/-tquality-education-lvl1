from framework.base_element import Base_element

class Frame(Base_element):

    def __init__(self, locator, name):
        super().__init__(locator, name)

    def go_to_frame(self):
        self.driver.switch_to.frame(self.find_element())

    def exit_frame(self):
        self.driver.switch_to.default_content()