import re
from waitress import serve
from constants import TABS
from helpers import PhoneFormatter
from checker.pts import check_pts
from checker.eniro import check_eniro
from checker.ratsit import check_ratsit
from checker.google import check_google
from flask import Flask, url_for, request
from htpy import html, body, button, form, input, div, a, main, ul
from components.main import html_footer, html_head, html_header

app = Flask(__name__, static_folder="static")


@app.route("/")
def index() -> str:
    return str(
        html(data_bs_theme="dark")[
            html_head(),
            body[
                div(".col-lg-7 .mx-auto .p-4 py-md-5")[
                    html_header(),
                    main[
                        form(
                            hx_post=url_for("init_check"),
                            hx_target=".results",
                        )[
                            div(".input-group .mb-3")[
                                input(".form-control", type="text", name="number"),
                                button(
                                    ".btn.btn-outline-primary.search-btn",
                                )["Sök"],
                            ]
                        ],
                        div(".results"),
                        html_footer(),
                    ],
                ]
            ],
        ]
    )


@app.route("/c/", methods=["POST"])
def init_check() -> str:
    number = request.form["number"]
    if not number or re.search("[a-zA-Z]", number):
        return "Ange ett giltigt telefonnummer."

    number = PhoneFormatter(number)._clean_number()

    return str(
        div[
            ul(".nav.nav-tabs.mb-3", role="tablist")[
                (tab.html_button for tab in TABS),
            ],
            div(".tab-content")[(tab.html_content(number) for tab in TABS)],
        ]
    )


@app.route("/c/pts/<number>", methods=["GET"])
def pts(number: str) -> str:
    return str(check_pts(number))


@app.route("/c/ratsit/<number>", methods=["GET"])
def ratsit(number: str) -> str:
    return "kkka"
    return str(check_ratsit(number))


@app.route("/c/eniro/<number>", methods=["GET"])
def eniro(number: str) -> str:
    return "kaka"
    return str(check_eniro(number))


@app.route("/c/google/<number>", methods=["GET"])
def google(number: str) -> str:
    return str(
        div[
            button(
                ".btn.btn-outline-primary",
                hx_post=url_for("google_search", number=number),
                hx_target="#google-results",
                **{"hx-on:click": "this.disabled=true"},
            )[f"Sök efter {number}"],
            a(
                ".btn.btn-outline-secondary.ms-2",
                href=f"https://www.google.se/search?q={number}",
                target="_blank",
            )[f"Öppna Google"],
            div("#google-results.mt-3"),
        ]
    )


@app.route("/c/google/<number>", methods=["POST"])
def google_search(number: str) -> str:
    return str(check_google(number))


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=9191)
