import requests  # type: ignore[import-untyped]
import datetime
from dataclasses import dataclass
from htpy import Element, button, div, h2, ul, li


@dataclass
class EniroHit:
    name: str

    @property
    def display_value(self) -> str:
        remove_strings = ["Vägbeskrivning", "Kolla lön"]
        fixed_name = self.name
        for string in remove_strings:
            fixed_name = fixed_name.replace(string, "")
        return fixed_name


def _get_companies(number: str) -> list[EniroHit]:
    response = requests.post(
        "http://localhost:9292/api/submit-scrape-job",
        json={
            "url": f"https://www.eniro.se/{number}/f%C3%B6retag",
            "elements": [
                {"name": "eniro", "xpath": '//h2[contains(@id, "company-link-name")]'}
            ],
            "user": "eniro",
            "time_created": str(datetime.datetime.now()),
        },
    )

    result_str = response.json()["eniro"][0]["text"]

    company_results: list[EniroHit] = []
    if result_str:
        companies = result_str.split(",")
        for company in companies:
            company_results.append(
                EniroHit(name=company),
            )
    return company_results


def _get_persons(number: str) -> list[EniroHit]:
    response = requests.post(
        "http://localhost:9292/api/submit-scrape-job",
        json={
            "url": f"https://www.eniro.se/{number}/personer",
            "elements": [
                {
                    "name": "eniro2",
                    "xpath": '//section/div[contains(@class, "rounded-4xl")]',
                }
            ],
            "user": "eniro2",
            "time_created": str(datetime.datetime.now()),
        },
    )
    if response.status_code != 200:
        raise AssertionError(f"Error: {response.status_code}, {response.content}")

    result_str = response.json()["eniro2"][0]["text"]

    person_results: list[EniroHit] = []
    if result_str:
        person_results.append(
            EniroHit(name=result_str),
        )
    return person_results


def check_eniro(number: str) -> Element:
    company_results = _get_companies(number)
    person_results = _get_persons(number)

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
                )[f"Personer: {len(person_results)} st"]
            ],
            div(
                "#persons.accordion-collapse.collapse.collapse",
                data_bs_parent="#accordionEniro",
            )[
                div(".accordion-body")[
                    ul[
                        (
                            li[person.display_value]
                            for person in person_results
                            if person_results
                        )
                    ],
                ]
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
                )[f"Företag: {len(company_results)} st"]
            ],
            div(
                "#companies.accordion-collapse.collapse",
                data_bs_parent="#accordionEniro",
            )[
                div(".accordion-body")[
                    ul[
                        (
                            li[company.display_value]
                            for company in company_results
                            if company_results
                        )
                    ],
                ]
            ],
        ],
    ]
