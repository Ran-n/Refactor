from astronaut import Astronaut
from rocket import Rocket

class GroundControl():

    planets = [
        ["moon", 24*3, "moon"],
        ["mars", 24*30*21, "planet"],
        ["pluto", 360*24*9.5, "planet?"]
    ]

    @staticmethod
    def mission(rocket, astronauts, destination):
        if len(rocket.get_crew()) == 0:
            result, work = False, 0
        elif rocket.get_fuel() == 9:
            results, work = False, 0
        elif destination[0] != GroundControl.planets[0][0] and destination[0] != GroundControl.planets[1][0] and destination[0] != GroundControl.planets[2][0]:
            result, work = False, 0
        else:
            result, work = rocket.travel(destination)

        def report(rocket, astronauts, result):
            return f"The travel has {'succeeded' if result else 'failed'}.\n{len(astronauts)} crew members.\nRocket has {rocket.get_fuel()} fuel left.\nCrew has worked {work} units."

        return result, work, report(rocket, astronauts, result)



rocket = Rocket()
rocket.set_name("Soyuz")
rocket.set_fuel(1000)
rocket.set_food(50)

astronauts = []
for i in range(3):
    astronauts.append(Astronaut("bob"+str(i), i))

rocket.set_crew(astronauts)

_, _, report = GroundControl.mission(rocket, astronauts, GroundControl.planets[0])
print(report)
