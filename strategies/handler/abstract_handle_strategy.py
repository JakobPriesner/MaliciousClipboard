from abc import ABC, abstractmethod

from model.event_type import EventType


class AbstractStrategy(ABC):
    @abstractmethod
    def can_handle(self, text: str, event_type: EventType) -> bool:
        """
        Check if the strategy can handle the message.

        :param text: clipboard text to check.
        :param event_type: event type to check.
        :return: True if the strategy can handle the message, otherwise False.
        """
        ...

    @abstractmethod
    def process_text(self, text: str, window_title: str, event_type: EventType) -> None:
        ...
