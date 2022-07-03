import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class TestExampleOne:
        def test_content_text(self):
            origion=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
            time.sleep(4)
            origion.click()
            origion.send_keys("New Delhi")
            origion.send_keys(Keys.ENTER)