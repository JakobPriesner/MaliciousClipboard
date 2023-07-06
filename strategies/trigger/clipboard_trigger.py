import platform
import time

import clipboard

from model.event_type import EventType
from strategies.trigger.abstract_trigger import AbstractTrigger


class ClipboardTrigger(AbstractTrigger):
    def monitor(self) -> None:
        while True:
            text = clipboard.paste()
            window_title = self._get_active_window_title()

            if text != self.least_recently_text:
                self.callback(text, window_title, EventType.ON_UPDATED_TEXT)

            time.sleep(0.125)
