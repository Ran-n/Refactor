from typing import Optional, List

from src.astronaut import Astronaut
from src.planet import Planet

class Rocket:
    __name: Optional[str]
    __fuel: Optional[int]
    __food: Optional[int]
    __crew: Optional[List[Astronaut]]

    def __init__(self, name:str = '', fuel:int = 0, food:int = 0, crew:List[Astronaut] = None) -> None:
        self.__name = name
        self.__fuel = fuel
        self.__food = food
        self.__crew = crew


    def set_name(self, new_name:str) -> None:
        self.__name = new_name
    def get_name(self) -> str:
        return self.__name

    def set_fuel(self, new_fuel:str) -> None:
        self.__fuel = new_fuel
    def get_fuel(self) -> str:
        return self.__fuel

    def set_food(self, new_food:str) -> None:
        self.__food = new_food
    def get_food(self) -> str:
        return self.__food

    def set_crew(self, new_crew:List[Astronaut]) -> None:
        self.__crew = new_crew
    def get_crew(self) -> List[Astronaut]:
        return self.__crew
    def add_2_crew(self, new_astronaut:Astronaut) -> None:
        if self.get_crew() is None:
            self.set_crew([new_astronaut])
        else:
            new_crew = self.get_crew()
            new_crew.append(new_astronaut)
            self.set_crew(new_crew)


    def launch(self) -> None:
        if self.get_fuel() > 10:
            self.set_fuel(self.get_fuel()-10)

    def fuel_per_hour(self) -> int:
        names = {
                'soyuz': 10,
                'n1': 10,
                'apollo': 8,
                'atlas': 9
        }

        return names[self.get_name().lower()]

    def food_per_day(self) -> int:
        return len(self.get_crew()) * 3

    def board_rocket(astronaut: Astronaut) -> None:
        self.add_2_crew(astronaut)
        astronaut.set_on_rocket()

    def travel(self, destination: Planet) -> (bool, int):
        total_work = 0
        food_needed =

        self.launch()

        # if fuel and food needed is less/equal than food
        if (self.get_fuel() >= (destination.get_time() * self.fuel_per_hour())) and ((self.food_per_day() * destination.get_time()/24) <= self.get_food()):
            for crew in self.get_crew():
                total_work += crew.work(destination.get_time())
            return True, total_work

        return False, total_work
