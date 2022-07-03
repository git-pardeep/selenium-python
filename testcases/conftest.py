import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()) #if not added in PATH
    driver.get("https://www.yatra.com/")
    wait=WebDriverWait(driver,10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait=wait

    yield driver
    driver.close()