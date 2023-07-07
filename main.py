import concurrent.futures
from typing import Type

from strategies.trigger import *


class ClipboardHandler:

    def start(self) -> None:
        trigger: list = [
            KeyboardTrigger,
            ClipboardTrigger,
        ]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.__start_trigger, trigger) for trigger in trigger]

            for th in threads:
                th.result()

    @staticmethod
    def __start_trigger(trigger: Type[AbstractTrigger]) -> None:
        trigger().monitor()


if __name__ == '__main__':
    ch = ClipboardHandler()
    ch.start()
