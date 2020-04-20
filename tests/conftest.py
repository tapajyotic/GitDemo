import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(executable_path="E:\TapoStudy\Pyhton\chromedriver_win32\chromedriver.exe",
                              options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\TapoStudy\geckodriver-v0.24.0-win64\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )