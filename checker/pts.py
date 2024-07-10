from htpy import Element, p
from checker.browser import chrome
from selenium.webdriver.common.by import By
import os
from playwright.sync_api import sync_playwright


def check_pts(number: str) -> Element:
    os.makedirs("/tmp")

    pw = sync_playwright().start()
    browser = pw.chromium.launch(
        headless=False,
        executable_path=os.environ["CHROME_PATH"],
    )
    page = browser.new_page()
    page.goto("https://nummer.pts.se/NbrSearch")

    search_field = page.get_by_role("textbox")
    search_field.fill(number)

    page.locator("button[type='submit']").click()

    result_text = page.locator("div .alert").inner_text()

    browser.close()

    return p[result_text]

    # driver = chrome()
    # driver.get("https://nummer.pts.se/NbrSearch")

    # # fill search input and perform search
    # driver.find_element(By.XPATH, "//input[@id='NbrToSearch']").send_keys(number)
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # # grab results from success alert
    # try:
    #     result = driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]")
    # except:
    #     result = driver.find_element(
    #         By.XPATH, "//span[contains(@class, 'field-validation-error')]"
    #     )

    # return p[result.text]
