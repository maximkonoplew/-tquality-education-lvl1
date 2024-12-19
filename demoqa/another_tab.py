from framework.base_form import Base_form
from loguru import logger

class Another_tab(Base_form):
    
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def switch_to_another_tab(self, number):
        window_handles = self.driver.window_handles
        desired_window = window_handles [number]
        self.driver.switch_to.window(desired_window)
