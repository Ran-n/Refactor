from astronaut import Astronaut
from rocket import Rocket
from ground_control import GroundControl

def main():
    rocket = Rocket("Soyuz", 1000, 50)
    for i in range(3):
        rocket.add_2_crew(Astronaut("bob"+str(i), i))

    planets = [
        ["moon", 24*3, "moon"],
        ["mars", 24*30*21, "planet"],
        ["pluto", 360*24*9.5, "planet?"]
    ]

    gc = GroundControl(planets)

    _, _, report = gc.mission(rocket, rocket.get_crew(), gc.get_planets()[0])
    print(report)

main()
