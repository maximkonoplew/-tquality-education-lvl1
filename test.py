from demoqa.main_page import Main_page
from demoqa.alert_page import Alert_page
from demoqa.frame_page import Frame_page
from demoqa.table_page import Table_page
from demoqa.handles_page import Handles_page
from demoqa.another_tab import Another_tab
from selenium.webdriver.common.by import By
from framework.datatestmanager import Datatestmanager
from loguru import logger

class Test:

    @staticmethod
    def test_alerts(go_to_main_page):  
        object_main_page = Main_page((By.XPATH, Datatestmanager.get_json_data("alerts", "locator_main_page")), Datatestmanager.get_json_data("alerts", "name_main_page"))
        assert object_main_page.find_element()

        object_main_page.go_to_alerts_frames_windows()
        object_alert_page = Alert_page((By.XPATH, Datatestmanager.get_json_data("alerts", "locator_alert_page")), Datatestmanager.get_json_data("alerts", "name_alert_page"))
        assert object_alert_page.go_to_alerts()

        assert object_alert_page.go_to_alertButton() == Datatestmanager.get_json_data("alerts", "alert_title")
        assert object_alert_page.find_element()

        confirm_result = object_alert_page.go_to_confirmButton() 
        assert confirm_result[0] == Datatestmanager.get_json_data("alerts", "alert_confirm_title")

        assert object_alert_page.find_element()
        assert confirm_result[1].text == Datatestmanager.get_json_data("alerts", "alert_confirm_result")

        prompt_result = object_alert_page.go_to_promptButton() 
        assert prompt_result[0] == Datatestmanager.get_json_data("alerts", "alert_prompt_title")

        assert object_alert_page.find_element()
        assert prompt_result[1].text == Datatestmanager.get_json_data("alerts", "alert_prompt_result")

    @staticmethod
    def test_frames(go_to_main_page):
        object_main_page = Main_page((By.XPATH, Datatestmanager.get_json_data("alerts", "locator_main_page")), Datatestmanager.get_json_data("alerts", "name_main_page"))
        assert object_main_page.find_element()

        object_main_page.go_to_alerts_frames_windows()
        object_frame_page = Frame_page((By.XPATH, Datatestmanager.get_json_data("frames", "locator_frame_page")), Datatestmanager.get_json_data("frames", "name_frame_page"))
        assert object_frame_page.go_to_nested_frames()
        result_check_nested_frames = object_frame_page.check_nested_frames()
        assert result_check_nested_frames[0] == Datatestmanager.get_json_data("frames", "name_parent_frame")
        assert result_check_nested_frames[1] == Datatestmanager.get_json_data("frames", "name_child_Iframe")

        assert object_frame_page.go_to_frames()
        result_check_frames = object_frame_page.check_frames()
        assert result_check_frames[0] == result_check_frames[1]

    @staticmethod
    def test_tables(go_to_main_page):
        object_main_page = Main_page((By.XPATH, Datatestmanager.get_json_data("alerts", "locator_main_page")), Datatestmanager.get_json_data("alerts", "name_main_page"))
        assert object_main_page.find_element()

        object_main_page.go_to_elements()
        object_table_page = Table_page((By.XPATH, Datatestmanager.get_json_data("tables", "locator_table_page")), Datatestmanager.get_json_data("tables", "name_table_page"))
        assert object_table_page.go_to_web_tables()

        object_table_page.add_new_user(1, ['Jon', 'Snow', 'knownothing@gmail.com', '30', '3000', 'alpha'])
        object_table_page.add_new_user(2, ['Ben', 'Forest', 'benforest@gmail.com', '20', '2000', 'beta'])
        object_table_page.delete_first_user()


    @staticmethod
    def test_handles(go_to_main_page):        
        object_main_page = Main_page((By.XPATH, "//div[@class='category-cards']"), "category-cards")
        assert object_main_page.find_element()

        object_main_page.go_to_alerts_frames_windows()
        object_browser_windows_page = Handles_page((By.XPATH, "//div[@class='left-pannel']"), "left-pannel")
        assert object_browser_windows_page.go_to_browser_windows()

        object_browser_windows_page.create_another_tab()
        object_another_tab = Another_tab((By.XPATH, "//*[@id='sampleHeading']"), 'sampleHeading')
        object_another_tab.switch_to_another_tab(1)
        assert object_another_tab.find_element()

        logger.info("4. Закрыть текущую вкладку")
        object_another_tab.driver.close()
        object_another_tab.switch_to_another_tab(0)
        assert object_browser_windows_page.find_element()

        assert object_browser_windows_page.go_to_links()
        object_browser_windows_page.go_to_main_page()
        object_another_tab = Another_tab((By.XPATH, "//div[@class='category-cards']"), "category-cards")

        object_another_tab.switch_to_another_tab(1)
        assert object_another_tab.find_element()

        logger.info("7. Переключиться на прошлую вкладку")
        object_another_tab.switch_to_another_tab(0)
        assert object_browser_windows_page.find_element()