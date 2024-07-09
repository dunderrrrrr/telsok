import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def chrome(headless: bool = True) -> WebDriver:
    DRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]
    CHROME_PATH = os.environ["CHROME_PATH"]
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"

    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument(f"user-agent={USER_AGENT}")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = CHROME_PATH
    return webdriver.Chrome(options=options, service=Service(DRIVER_PATH))
