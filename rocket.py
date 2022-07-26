from typing import Optional, List

from astronaut import Astronaut

class Rocket:
    __name: Optional[str]
    __fuel: Optional[int]
    __food: Optional[int]
    __crew: Optional[List[Astronaut]]

    def __init__(self, name:str = '', fuel:int = 0, food:int = 0, crew:List[Astronaut] = None):
        self.__name = name
        self.__fuel = fuel
        self.__food = food
        self.__crew = crew


    def set_name(self, new_name:str):
        self.__name = new_name
    def get_name(self):
        return self.__name

    def set_fuel(self, new_fuel:str):
        self.__fuel = new_fuel
    def get_fuel(self):
        return self.__fuel

    def set_food(self, new_food:str):
        self.__food = new_food
    def get_food(self):
        return self.__food

    def set_crew(self, new_crew:List[Astronaut]):
        self.__crew = new_crew
    def get_crew(self):
        return self.__crew
    def add_2_crew(self, new_astronaut:Astronaut):
        self.set_crew(self.get_crew().append(astronaut))


    def launch(self):
        if self.get_fuel() > 10:
            self.set_fuel(self.get_fuel()-10)

    def fuel_per_hour(self):
        names = {
                'soyuz': 10,
                'n1': 10,
                'apollo': 8,
                'atlas': 9
        }

        return names[self.get_name().lower()]

    def food_per_day(self):
        return len(self.get_crew()) * 3

    def travel(self, destination):
        self.launch()
        time = destination[1]
        consume = self.fuel_per_hour()
        total = time * consume

        food_needed = self.food_per_day() * time/24

        total_work = 0
        if self.get_fuel() >= total and food_needed <= self.get_food():
            for crew in self.get_crew():
                total_work += crew.work(time)
            return True, total_work
        else:
            return False, total_work

    def board_rocket(astronaut):
        self.add_2_crew(astronaut)
        astronaut.set_on_rocket()
