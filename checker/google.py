import os
from dotenv import load_dotenv
from htpy import Element, div, ul, li, a, p
from googleapiclient.discovery import build  # type: ignore[import-untyped]

load_dotenv()


def check_google(number: str) -> Element:
    try:
        API_KEY = os.environ["GOOGLE_API_KEY"]
    except:
        return p["Missing API key."]

    service = build("customsearch", "v1", developerKey=API_KEY)
    res = (
        service.cse()
        .list(
            q=number,
            lr="lang_sv",
            cx="13a078aa34950448a",
        )
        .execute()
    )
    if "items" in res:
        return div[
            ul[
                (
                    li[a(href=item["link"], target="_blank")[item["title"]]]
                    for item in res["items"]
                )
            ]
        ]
    else:
        return p["Inga resultat."]
