from framework.chrome import Chrome
from framework.datatestmanager import Datatestmanager

class Alert():

    def __init__(self):
        self.driver = Chrome().driver
        self.alert = self.driver.switch_to.alert

    def get_text_from_alert(self):
        return self.alert.text
    
    def close_alert(self):
        self.alert.accept()

    def write_alert(self):
        self.alert.send_keys(Datatestmanager.get_json_data("alerts", "name_alert_prompt"))