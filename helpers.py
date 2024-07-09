from functools import wraps
from dataclasses import dataclass
from flask import redirect, url_for
from flask import request, redirect, url_for


def htmx_view(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not "HX-Request" in request.headers:
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function


@dataclass
class PhoneFormatter:
    number: str

    def _clean_number(self) -> str:
        chars_to_remove = " ()-–/\u202d\u202c"

        formatted_phone = self.number
        for char in chars_to_remove:
            formatted_phone = formatted_phone.replace(char, "")

        if self.number.startswith("+46"):
            formatted_phone = formatted_phone.replace("+46", "0")

        return formatted_phone
