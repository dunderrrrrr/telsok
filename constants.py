from flask import url_for
from dataclasses import dataclass
from htpy import Element, button, div, li, span, p


@dataclass
class Tab:
    name: str
    active: bool = False

    @property
    def identifier(self) -> str:
        return self.name.lower()

    @property
    def html_button(self) -> Element:
        return li(".nav-item", role="presentation")[
            button(
                f"#{self.identifier}-tab.nav-link.active"
                if self.active
                else f"#{self.identifier}-tab.nav-link",
                data_bs_toggle="tab",
                data_bs_target=f"#{self.identifier}",
                type="button",
                role="tab",
                aria_controls=self.identifier,
                aria_selected="true",
            )[
                f"{self.name} ",
                div(
                    f"#{self.identifier}-loading.spinner-border.spinner-border-sm.htmx-indicator.my-indicator",
                    role="status",
                )[span(".visually-hidden")["Loading..."]],
            ]
        ]

    def html_content(self, number: str) -> Element:
        return div(
            f"#{self.identifier}.tab-pane.fade.show.active"
            if self.active
            else f"#{self.identifier}.tab-pane.fade",
            role="tabpanel",
            aria_labelledby=f"{self.identifier}-tab",
            hx_get=url_for(self.identifier, number=number),
            hx_trigger="load",
            hx_indicator=f"#{self.identifier}-loading",
            hx_disabled_elt=".search-btn",
        )[f"Våra hamstrar hämtar data, vänta lite... 🐹"]


TABS = [
    Tab("PTS", True),
    Tab("Ratsit"),
    Tab("Eniro"),
    Tab("Google"),
]
