from flask import url_for
from htpy import title, head, script, script, link, header, a, footer, meta, p


def html_head() -> str:
    return str(
        head[
            title["TelSök.se - Sök telefonnummer. Överallt!"],
            meta(charset="UTF-8"),
            meta(name="description", content="TelSök - Sök telefonnummer. Överallt!"),
            meta(name="keywords", content="sök, telefonnummer, mobilnummer, hitta"),
            script(src="https://unpkg.com/htmx.org@2.0.0"),
            script(
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            ),
            link(
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                rel="stylesheet",
            ),
            link(
                href="https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&display=swap",
                rel="stylesheet",
            ),
            link(href=f'{url_for("static", filename="style.css")}', rel="stylesheet"),
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
                "TelSök är ett verktyg för att underlätta sökning av telefonnummer genom att använda publika sökmotorer."
                "Datan som presenteras hämtas från pts.se, ratsit.se, eniro.se och google.se. Vi sparar ingen information."
            ],
        ],
    )
