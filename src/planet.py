class Planet:
    __name: str
    __time: int
    __category: str

    def __init__(self, name: str, time: int, category: str) -> None:
        self.__name = name
        self.__time = time
        self.__category = category


    def get_name(self) -> str:
        return self.__name
    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_time(self) -> int:
        return self.__time
    def set_time(self, new_time: int) -> None:
        self.__time = new_time

    def get_category(self) -> str:
        return self.__category
    def set_category(self, new_category) -> None:
        self.__category = new_category
