from dataclasses import dataclass


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
