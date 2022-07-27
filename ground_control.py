from astronaut import Astronaut
from rocket import Rocket

class GroundControl:

    def __init__(self, planets):
        self.__planets = planets


    def get_planets(self):
        return self.__planets
    def set_planets(self, new_planets):
        self.__planets = new_planets


    def mission(self, rocket, astronauts, destination):
        if len(rocket.get_crew()) == 0:
            result, work = False, 0
        elif rocket.get_fuel() == 9:
            results, work = False, 0
        elif destination[0] != self.__planets[0][0] and destination[0] != self.__planets[1][0] and destination[0] != self.__planets[2][0]:
            result, work = False, 0
        else:
            result, work = rocket.travel(destination)

        def report(rocket, astronauts, result):
            return f"The travel has {'succeeded' if result else 'failed'}.\n{len(astronauts)} crew members.\nRocket has {rocket.get_fuel()} fuel left.\nCrew has worked {work} units."

        return result, work, report(rocket, astronauts, result)
