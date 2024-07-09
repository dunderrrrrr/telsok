from htpy import Element, p
from checker.browser import chrome
from selenium.webdriver.common.by import By


def check_pts(number: str) -> Element:
    driver = chrome()
    driver.get("https://nummer.pts.se/NbrSearch")

    # fill search input and perform search
    driver.find_element(By.XPATH, "//input[@id='NbrToSearch']").send_keys(number)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # grab results from success alert
    try:
        result = driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]")
    except:
        result = driver.find_element(
            By.XPATH, "//span[contains(@class, 'field-validation-error')]"
        )

    return p[result.text]
