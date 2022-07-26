from astronaut import Astronaut
from rocket import Rocket
from ground_control import GroundControl

astronauts = []
for i in range(3):
    astronauts.append(Astronaut("bob"+str(i), i))

rocket = Rocket("Soyuz", 1000, 50, astronauts)

_, _, report = GroundControl.mission(rocket, astronauts, GroundControl.planets[0])
print(report)
