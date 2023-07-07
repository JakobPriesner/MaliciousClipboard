import datetime
import re
from pathlib import Path

from model.event_type import EventType
from strategies.handler import AbstractStrategy
import pyscreenshot


class ScreenshotStrategy(AbstractStrategy):
    def can_handle(self, text: str, event_type: EventType) -> bool:
        return text != "" and (event_type == EventType.ON_KEYBOARD_PASTE)

    def process_text(self, text: str, window_title: str, event_type: EventType) -> None:
        path = Path(__file__).parent.parent.parent / 'screenshots' / f"{self._get_date_string()}_{text[:50].replace(' ', '_')}.png"
        screenshot = pyscreenshot.grab()
        screenshot.save(path.absolute())

    @staticmethod
    def _encode_string_for_filename(text: str) -> str:
        valid_chars = re.sub(r'[^\w\s\-_.()]+', '', text)
        return re.sub(r'\s+', '_', valid_chars)

    @staticmethod
    def _get_date_string() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")