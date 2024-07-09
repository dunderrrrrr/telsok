from flask import url_for
from htpy import title, head, script, script, link, header, a, footer, meta, p, span


def html_head() -> str:
    stylesheets = [
        "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        "https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&display=swap",
        url_for("static", filename="style.css"),
    ]
    scripts = [
        "https://unpkg.com/htmx.org@2.0.0",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
    ]
    return str(
        head[
            title["TelSök.se - Sök telefonnummer. Överallt!"],
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            meta(name="description", content="TelSök - Sök telefonnummer. Överallt!"),
            meta(name="keywords", content="sök, telefonnummer, mobilnummer, hitta"),
            (script(src=_script) for _script in scripts),
            (link(href=stylesheet, rel="stylesheet") for stylesheet in stylesheets),
        ],
    )


def html_header() -> str:
    return str(
        header(".d-flex.align-items-center.pb-3.mb-3")[
            a(
                ".logo.d-flex.align-items-center.text-body-emphasis.text-decoration-none",
                href=url_for("index"),
            )["TelSök.se"]
        ],
    )


def html_footer() -> str:
    return str(
        footer(".pt-5.my-5.text-body-secondary.border-top")[
            p["TelSök · 2024"],
            p(".info")[
                "TelSök är ett verktyg för att underlätta sökning av telefonnummer genom att använda olika sökmotorer och APIer. "
                "Datan som presenteras hämtas från inabler.se, ratsit.se, eniro.se och google.se. Vi sparar ingen information "
                "och sökningarna görs i realtid."
            ],
        ],
    )
