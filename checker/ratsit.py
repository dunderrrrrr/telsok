import requests
from dataclasses import dataclass
from htpy import Element, button, div, h2, ul, li, a, span, p


@dataclass
class RatsitHit:
    name: str
    address: str
    url: str

    @property
    def display_value(self) -> str:
        return str(
            span[
                a(href=self.url, target="_blank")[f"{self.name}"],
                span[f" {self.address}"],
            ]
        )


def check_ratsit(number: str) -> Element:
    response = requests.post(
        "https://www.ratsit.se/api/search/combined",
        json={
            "who": number,
            "phoneticSearch": True,
            "page": 1,
            "url": "/sok/foretag?vem=0760531600",
        },
    )

    if response.status_code != 200:
        return p["Någonting gick fel..."]

    company_results: list[RatsitHit] = []
    company_hits = response.json()["company"]["hits"]
    if len(company_hits):
        for company in company_hits:
            company_results.append(
                RatsitHit(
                    name=company["companyName"],
                    address=company["address"],
                    url=company["companyUrl"],
                )
            )

    person_results: list[RatsitHit] = []
    person_hits = response.json()["person"]["hits"]
    if len(person_hits):
        for person in person_hits:
            person_results.append(
                RatsitHit(
                    name=f'{person["firstName"]} {person["lastName"]} ({person["age"]})',
                    address=f', {person["streetAddress"]}, {person["city"]}',
                    url=person["personUrl"],
                )
            )

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
                )[f"Personer: {len(person_hits)} st"]
            ],
            div(
                "#persons.accordion-collapse.collapse.collapse",
                data_bs_parent="#accordionRatsit",
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
                )[f"Företag: {len(company_hits)} st"]
            ],
            div(
                "#companies.accordion-collapse.collapse",
                data_bs_parent="#accordionRatsit",
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
