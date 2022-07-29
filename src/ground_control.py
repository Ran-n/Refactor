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


    def get_planet_names(self) -> List[Planet]:
        return [ele.get_name() for ele in self.get_planets()]


    def report(self, rocket: Rocket, astronauts: Astronaut, result: bool, work: int) -> str:
        return f"The travel has {'succeeded' if result else 'failed'}.\n"+\
        f"{len(astronauts)} crew members.\n"+\
        f"Rocket has {rocket.get_fuel()} fuel left.\n"+\
        f"Crew has worked {work} units."

    def mission(self, rocket: Rocket, astronauts: Astronaut, destination: Planet) -> (bool, int, str):
        if (len(rocket.get_crew()) == 0) or (rocket.get_fuel() == 9) or (destination.get_name() not in self.get_planet_names()):
            result, work = False, 0
        else:
            result, work = rocket.travel(destination)

        return result, work, self.report(rocket, astronauts, result, work)
