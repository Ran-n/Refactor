from typing import Optional

class Astronaut:
    __name: Optional[str]
    __work_unit: Optional[int]
    __on_rocket: False

    def __init__(self, name: str, work_unit: int, on_rocket: bool = False) -> None:
        self.__name = name
        self.__work_unit = work_unit
        self.__on_rocket = on_rocket


    def get_name(self) -> str:
        return self.__name
    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_work_unit(self) -> int:
        return self.__work_unit
    def set_work_unit(self, new_work_unit: int) -> None:
        self.__work_unit = new_work_unit

    def set_on_rocket(self, on_rocket: bool = True) -> int:
        self.__on_rocket = on_rocket
    def is_on_rocket(self) -> None:
        return self.__on_rocket


    def work(self, time: int) -> int:
        return self.get_work_unit() * time
