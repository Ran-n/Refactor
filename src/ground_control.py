from typing import Optional, List

from src.astronaut import Astronaut
from src.rocket import Rocket
from src.planet import Planet

class GroundControl:

    __planets: List[Planet]

    def __init__(self, planets: Optional[List[Planet]] = None):
        self.__planets = planets


    def get_planets(self) -> List[Planet]:
        return self.__planets
    def set_planets(self, new_planets: List[Planet]) -> None:
        self.__planets = new_planets


    def mission(self, rocket, astronauts, destination):
        if len(rocket.get_crew()) == 0:
            result, work = False, 0
        elif rocket.get_fuel() == 9:
            results, work = False, 0
        elif destination.get_name() != self.get_planets()[0].get_name() and destination.get_name() != self.get_planets()[1].get_name() and destination.get_name() != self.get_planets()[2].get_name():
            result, work = False, 0
        else:
            result, work = rocket.travel(destination)

        def report(rocket, astronauts, result):
            return f"The travel has {'succeeded' if result else 'failed'}.\n{len(astronauts)} crew members.\nRocket has {rocket.get_fuel()} fuel left.\nCrew has worked {work} units."

        return result, work, report(rocket, astronauts, result)
