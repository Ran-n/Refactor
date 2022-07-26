from rocket import Rocket
from typing import Optional

class Astronaut:
    __name: Optional[str]
    __work_unit: Optional[int]
    __on_rocket: False

    def __init__(self, name: str, work_unit: int, on_rocket: bool = False):
        self.__name = name
        self.__work_unit = work_unit
        self.__on_rocket = on_rocket


    def get_name(self):
        return self.__name
    def set_name(self, new_name: str):
        self.__name = new_name

    def get_work_unit(self):
        return self.__work_unit
    def set_work_unit(self, new_work_unit: int):
        self.__work_unit = new_work_unit

    def set_on_rocket(self, on_rocket: bool = True):
        self.__on_rocket = on_rocket
    def is_on_rocket(self):
        return self.__on_rocket


    def work(self, time: int):
        return self.get_work_unit() * time


    # xFCR: move
    @staticmethod
    def board_rocket(rocket, astronaut):
        rocket.get_crew().append(astronaut)
        astronaut.set_on_rocket()
