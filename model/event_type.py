from enum import Enum


class EventType(Enum):
    ON_KEYBOARD_COPY = 1
    ON_KEYBOARD_PASTE = 2
    ON_PASTE = 3
    ON_UPDATED_TEXT = 4
