from framework.base_form import Base_form
from demoqa.button import Button
from demoqa.text import Text
from demoqa.alert import Alert
from selenium.webdriver.common.by import By
from loguru import logger


class Alert_page(Base_form):
    __BUTTON_ALERTS_LEFT_PANNEL = Button((By.XPATH, "//span[contains(text(), 'Alerts')]"), 'Button Alerts')
    __TITLE = Text((By.XPATH, "//*[@class='text-center']"), "Title Alerts")
    __ALERT_BUTTON = Button((By.XPATH, "//button[@id='alertButton']"), "alertButton")
    __CONFIRM_BUTTON = Button((By.XPATH, "//button[@id='confirmButton']"), "confirmButton")
    __CONFITM_RESULT = Text((By.XPATH, "//span[@id='confirmResult']"), "confirmResult")
    __PROMPT_BUTTON = Button((By.XPATH, "//button[@id='promtButton']"), "promtButton")
    __PROMPT_RESULT = Text((By.XPATH, "//span[@id='promptResult']"), "promptResult")
    
    def __init__(self, locator, name):
        super().__init__(locator, name)
    
    def go_to_alerts(self):
        logger.info("2. На открывшейся странице в левом меню кликнуть пункт Alerts")
        self.__BUTTON_ALERTS_LEFT_PANNEL.find_click_element()
        return self.__TITLE.wait_element()
    
    def go_to_alertButton(self):
        logger.info("3. Нажать на кнопку Click Button to see alert")
        self.__ALERT_BUTTON.find_click_element()
        alert = Alert()
        alert_text = alert.get_text_from_alert()
        logger.info("4. Нажать на кнопку OK")
        alert.close_alert()
        return alert_text
    
    def go_to_confirmButton(self):
        logger.info("5. Нажать на кнопку On button click, confirm box will appear")
        self.__CONFIRM_BUTTON.find_click_element()
        alert = Alert()
        alert_text = alert.get_text_from_alert()
        logger.info("6. Нажать на кнопку OK")
        alert.close_alert()
        confirm_result = self.__CONFITM_RESULT.find_element()
        return alert_text, confirm_result
    
    def go_to_promptButton(self):
        logger.info("7. Нажать на кнопку On button click, prompt box will appear")
        self.__PROMPT_BUTTON.find_click_element()
        alert = Alert()
        alert_text = alert.get_text_from_alert()
        logger.info("8. Ввести случайно сгенерированный текст")
        alert.write_alert()
        logger.info("8. Hажать на кнопку OK")
        alert.close_alert()
        prompt_result = self.__PROMPT_RESULT.find_element()
        return alert_text, prompt_result
    