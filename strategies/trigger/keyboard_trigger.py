import time

import clipboard
import pyautogui
import pygame

from model.event_type import EventType
from strategies.trigger.abstract_trigger import AbstractTrigger


class KeyboardTrigger(AbstractTrigger):
    def monitor(self) -> None:
        while True:
            print("handle action")
            self.__handle_keyboard_action()
            time.sleep(0.25)

    def __handle_keyboard_action(self) -> None:
        print("doing some stuff")
        keys = pygame.key.get_pressed()
        print(keys)

        if not keys[pygame.K_LCTRL]:
            return

        if keys[pygame.K_v]:
            print("paste")
            text: str = clipboard.paste()
            window_title: str = self._get_active_window_title()
            self.callback(text, window_title, EventType.ON_KEYBOARD_PASTE)

        if keys[pygame.K_c]:
            print("copy")
            text: str = clipboard.paste()
            window_title: str = self._get_active_window_title()
            self.callback(text, window_title, EventType.ON_KEYBOARD_COPY)