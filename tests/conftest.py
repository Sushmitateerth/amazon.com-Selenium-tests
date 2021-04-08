import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\steerth\\Desktop\\browserfiles\\chromedriver.exe")
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()
