import platform

import clipboard
from pynput.keyboard import Listener as key_listener, Key

from model.event_type import EventType
from strategies.trigger.abstract_trigger import AbstractTrigger


class KeyboardTrigger(AbstractTrigger):
    def __init__(self) -> None:
        super().__init__()
        self.ctrl_pressed: bool = False

    def monitor(self) -> None:
        with key_listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, event) -> None:
        if event == Key.cmd or event == Key.ctrl_l or event == Key.ctrl_r:
            self.ctrl_pressed = True

        if not self.ctrl_pressed:
            return

        if not hasattr(event, "char"):
            return

        if event.char == "v" or event.char == "x":
            text: str = clipboard.paste()
            window_title: str = self._get_active_window_title()
            self.callback(text, window_title, EventType.ON_KEYBOARD_PASTE)

        if event.char == "c":
            text: str = clipboard.paste()
            window_title: str = self._get_active_window_title()
            self.callback(text, window_title, EventType.ON_KEYBOARD_COPY)

    def on_release(self, event) -> None:
        if event == Key.cmd or event == Key.ctrl_l or event == Key.ctrl_r:
            self.ctrl_pressed = False
