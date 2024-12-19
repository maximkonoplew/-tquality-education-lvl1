import pytest
from framework.chrome import Chrome
from framework.configmanager import ConfigManager

@pytest.fixture
def go_to_main_page():
    Chrome().driver.get(ConfigManager.get_json_data("browser", "start_url"))