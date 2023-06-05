from abc import ABC, abstractmethod

from model.event_type import EventType
from strategies.handler.abstract_handle_strategy import AbstractStrategy
from strategies.handler.log_strategy import LogStrategy


class AbstractTrigger(ABC):
    def __init__(self):
        self.strategies: list[AbstractStrategy] = [
            LogStrategy()
        ]
        self.least_recently_text: str = ""
        self.least_recently_window: str = ""

    @abstractmethod
    def monitor(self) -> None:
        ...

    def callback(self, text: str, window_title: str, event_type: EventType) -> None:
        print("callback")
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
        return "todo"  # todo
