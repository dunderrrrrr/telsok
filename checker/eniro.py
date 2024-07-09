import time
from checker.browser import chrome
from selenium.webdriver.common.by import By
from htpy import Element, button, div, h2, ul, li, p


def _clean_text(text: str) -> str:
    text = text.replace("Vägbeskrivning", "")
    return text.replace("Kolla lön", "")


def check_eniro(number: str) -> Element:
    driver = chrome()
    driver.get(f"https://www.eniro.se/{number}/f%C3%B6retag")
    time.sleep(2)
    persons = []

    # accept cookie popup
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'GODKÄNN')]").click()
    except:
        pass

    # grab company titles
    company_titles = [
        element.text
        for element in driver.find_elements(
            By.XPATH, "//div[contains(@data-guv-impression,'company_card')]//h2"
        )
    ]

    # check navigation links
    try:
        company_link, persons_link = driver.find_elements(
            By.XPATH, "//nav[contains(@aria-label,'Change result type')]//p"
        )
    except:
        not_found = driver.find_element(By.XPATH, "//h1").text
        return p[not_found]

    persons_count = int(persons_link.text.split("\n")[1])

    # if there are persons, grab them
    if persons_count:
        persons_link.click()
        time.sleep(2)
        persons = [
            _clean_text(a.text)
            for a in driver.find_elements(
                By.XPATH, "//div[contains(@class,'relative')]"
            )
            if a.text
        ]

    return div("#accordionEniro.accordion")[
        div(".accordion-item")[
            h2(".accordion-header")[
                button(
                    ".accordion-button.collapsed",
                    type="button",
                    data_bs_toggle="collapse",
                    data_bs_target="#persons",
                    aria_expanded="false",
                    aria_controls="persons",
                )[f"Personer: {persons_count} st"]
            ],
            div(
                "#persons.accordion-collapse.collapse.collapse",
                data_bs_parent="#accordionEniro",
            )[
                div(".accordion-body")[ul[(li[person] for person in persons)],]
            ],
        ],
        div(".accordion-item")[
            h2(".accordion-header")[
                button(
                    ".accordion-button.collapsed",
                    type="button",
                    data_bs_toggle="collapse",
                    data_bs_target="#companies",
                    aria_expanded="false",
                    aria_controls="companies",
                )[f"Företag: {len(company_titles)} st"]
            ],
            div(
                "#companies.accordion-collapse.collapse",
                data_bs_parent="#accordionEniro",
            )[
                div(".accordion-body")[ul[(li[title] for title in company_titles)],]
            ],
        ],
    ]
