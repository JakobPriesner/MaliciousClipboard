import concurrent.futures

from strategies.handler.abstract_handle_strategy import AbstractStrategy
from strategies.handler import LogStrategy
from strategies.trigger import *


class ClipboardHandler:
    def __init__(self):
        self.strategies: list[AbstractStrategy] = [
            LogStrategy()
        ]

    def start(self) -> None:
        trigger: list = [
            ClipboardTrigger,
            KeyboardTrigger
        ]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.__start_trigger, trigger) for trigger in trigger]
            for th in threads:
                th.result()

    @staticmethod
    def __start_trigger(trigger: AbstractTrigger) -> None:
        trigger().monitor()


if __name__ == '__main__':
    ch = ClipboardHandler()
    ch.start()
