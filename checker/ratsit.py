import time
from checker.browser import chrome
from selenium.webdriver.common.by import By
from htpy import Element, button, div, h2, ul, li


def _clean_text(text: str) -> str:
    if "gav inga träffar" in text:
        return text.split(".")[0]
    return text.replace("Se lön direkt", "")


def _split_toggler_text(text: str) -> int:
    return int(text.split(" ")[1])


def check_ratsit(number: str) -> Element:
    driver = chrome()
    driver.get(f"https://www.ratsit.se/sok/foretag?vem={number}")

    time.sleep(5)

    # accept cookie popup
    try:
        driver.find_element(
            By.XPATH, "//*[contains(text(), 'Tillåt alla cookies')]"
        ).click()
    except:
        pass

    # the "persons/companies-toggler"
    toggler = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'search-segment')]//a"
    )

    # grab persons link and counts
    persons_link = toggler[0]
    persons_count = _split_toggler_text(persons_link.text)

    # grab companies link and counts
    companies_link = toggler[1]
    companies_count = _split_toggler_text(companies_link.text)

    # get companies data
    companies = [
        _clean_text(a.text)
        for a in driver.find_elements(
            By.XPATH, "//div[contains(@class, 'search-result-list-holder d-block')]"
        )
        if a.text
    ]

    # move to persons and get persons data
    persons_link.click()
    persons = [
        _clean_text(a.text)
        for a in driver.find_elements(
            By.XPATH, "//div[contains(@class, 'search-result-list-holder d-block')]"
        )
        if a.text
    ]

    return div("#accordionRatsit.accordion")[
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
                data_bs_parent="#accordionRatsit",
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
                )[f"Företag: {companies_count} st"]
            ],
            div(
                "#companies.accordion-collapse.collapse",
                data_bs_parent="#accordionRatsit",
            )[
                div(".accordion-body")[ul[(li[company] for company in companies)],]
            ],
        ],
    ]
