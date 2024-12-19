from framework.base_form import Base_form
from demoqa.button import Button
from demoqa.text import Text
from demoqa.frame import Frame
from selenium.webdriver.common.by import By
from loguru import logger


class Frame_page(Base_form):
    __BUTTON_NESTED_FRAMES_LEFT_PANNEL = Button((By.XPATH, "//span[contains(text(), 'Nested Frames')]"), "button_frames_left_pannel")
    __TITLE = Text((By.XPATH, "//*[@class='text-center']"), "Title Frames")
    __PARENT_FRAME = Frame((By.XPATH, "//iframe[@id='frame1']"), "frame1")
    __NAME_PARENT_FRAME = Text((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent frame")
    __CHILD_FRAME = Frame((By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']"), "Child Iframe")
    __NAME_CHILD_FRAME = Text((By.XPATH, "//p[contains(text(), 'Child Iframe')]"), "Child Iframe")
    __BUTTON_FRAMES_LEFT_PANNEL = Button((By.XPATH, "//span[contains(text(), 'Frames')]"), "button_frames_left_pannel")
    __BIG_FRAME = Frame((By.XPATH, "//iframe[@id='frame1']"), "frame1")
    __NAME_BIG_FRAME = Text((By.XPATH, "//*[contains(text(), 'This is a sample page')]"), "frame1_inscription")
    __SMALL_FRAME = Frame((By.XPATH, "//iframe[@id='frame2']"), "frame2")
    __NAME_SMALL_FRAME = Text((By.XPATH, "//*[contains(text(), 'This is a sample page')]"), "frame2_inscription")
    
    def __init__(self, locator, name):
        super().__init__(locator, name)
    
    def go_to_nested_frames(self):
        logger.info("2. На открывшейся странице в левом меню кликнуть пункт Nested Frames")
        self.__BUTTON_NESTED_FRAMES_LEFT_PANNEL.find_click_element()
        return self.__TITLE.wait_element()
    
    def check_nested_frames(self):
        self.__PARENT_FRAME.go_to_frame()
        name_parent_frame = self.__NAME_PARENT_FRAME.find_element().text
        self.__CHILD_FRAME.go_to_frame()
        name_child_frame = self.__NAME_CHILD_FRAME.find_element().text
        self.__CHILD_FRAME.exit_frame()
        return name_parent_frame, name_child_frame
    
    def go_to_frames(self):
        logger.info("3. В левом меню выбрать пункт Frames")
        self.__BUTTON_FRAMES_LEFT_PANNEL.find_click_element()
        return self.__TITLE.wait_element()

    def check_frames(self):
        self.__BIG_FRAME.go_to_frame()
        name_big_frame = self.__NAME_BIG_FRAME.find_element().text
        self.__BIG_FRAME.exit_frame()

        self.__SMALL_FRAME.go_to_frame()
        name_small_frame = self.__NAME_SMALL_FRAME.find_element().text
        self.__SMALL_FRAME.exit_frame()
        return name_big_frame, name_small_frame