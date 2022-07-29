from typing import Optional, List

from src.exceptions import UnknownPlanet

from src.astronaut import Astronaut
from src.rocket import Rocket
from src.planet import Planet

class GroundControl:

    __planets: List[Planet]
    __mission_result: Optional[bool]
    __work: Optional[int]

    def __init__(self, planets: Optional[List[Planet]] = None, mission_result: Optional[bool] = None, work: Optional[int] = None) -> None:
        self.__planets = planets
        self.__mission_result = mission_result
        self.__work = work


    def get_planets(self) -> List[Planet]:
        return self.__planets
    def set_planets(self, new_planets: List[Planet]) -> None:
        self.__planets = new_planets

    def get_planet(self, position: int) -> Planet:
        try:
            return self.get_planets()[position]
        except IndexError:
            raise UnknownPlanet(f'The planet with position {position} is unknown.')
        except:
            raise
    def set_planet(self, position: int, new_planet: Planet) -> None:
        try:
            self.__planets[position] = new_planet
        except IndexError:
            raise UnknownPlanet(f'The planet with position {position} is unknown.')
        except:
            raise

    def get_mission_result(self) -> bool:
        return self.__mission_result
    def set_mission_result(self, new_result: bool) -> None:
        self.__mission_result = new_result

    def get_work(self) -> int:
        return self.__work
    def set_work(self, new_work: int) -> None:
        self.__work = new_work


    def set_mission_parameters(self, result: bool, work: int) -> None:
        self.set_mission_result(result)
        self.set_work(work)
    def get_mission_parameters(self) -> (bool, int):
        return self.get_mission_result(), self.get_work()


    def get_planet_names(self) -> List[Planet]:
        return [ele.get_name() for ele in self.get_planets()]


    def report(self, rocket: Rocket, astronauts: Astronaut, result: bool, work: int) -> str:
        return f"The travel has {'succeeded' if result else 'failed'}.\n"+\
        f"{len(astronauts)} crew members.\n"+\
        f"Rocket has {rocket.get_fuel()} fuel left.\n"+\
        f"Crew has worked {work} units."

    def mission(self, rocket: Rocket, astronauts: Astronaut, destination: Planet) -> (bool, int, str):
        if (len(rocket.get_crew()) == 0) or (rocket.get_fuel() == 9) or (destination.get_name() not in self.get_planet_names()):
            self.set_mission_parameters(False, 0)
        else:
            self.set_mission_parameters(*rocket.travel(destination))

        return self.report(rocket, astronauts, *self.get_mission_parameters())
