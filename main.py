from astronaut import Astronaut
from rocket import Rocket
from ground_control import GroundControl

def main():
    rocket = Rocket("Soyuz", 1000, 50)
    for i in range(3):
        rocket.add_2_crew(Astronaut("bob"+str(i), i))

    _, _, report = GroundControl.mission(rocket, rocket.get_crew(), GroundControl.planets[0])
    print(report)

main()
