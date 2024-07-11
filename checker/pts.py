import requests  # type: ignore[import-untyped]
from htpy import Element, p
from requests.exceptions import ConnectionError  # type: ignore[import-untyped]


def check_pts(number: str) -> Element:
    try:
        response = requests.get(
            f"https://www.inabler.se/ocean/nosearch.php?number={number}"
        )
    except ConnectionError:
        return p["Någonting gick fel."]

    if response.status_code == 200:
        return p[response.content.decode()]
    else:
        return p[f"Felkod: {response.status_code}"]
