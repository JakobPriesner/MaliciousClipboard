from datetime import datetime
from pathlib import Path

from model.event_type import EventType
from strategies.handler import AbstractStrategy


class LogStrategy(AbstractStrategy):
    def can_handle(self, text: str, event_type: EventType) -> bool:
        return text != "" and (event_type == EventType.ON_UPDATED_TEXT or event_type == EventType.ON_KEYBOARD_COPY)

    def process_text(self, text: str, window_title: str, event_type: EventType) -> None:
        log_file_path = Path(__file__).parent.parent.parent / "log" / "clipboard.log"
        with open(log_file_path, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}] title: '{window_title}', text: '{text}'\n")
