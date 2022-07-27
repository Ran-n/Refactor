#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
from src.astronaut import Astronaut
from src.rocket import Rocket
from src.ground_control import GroundControl
from src.planet import Planet

def main():
    rocket = Rocket("Soyuz", 1000, 50)
    for i in range(3):
        rocket.add_2_crew(Astronaut("bob"+str(i), i))

    planets = [
            Planet("moon", 24*3, "moon"),
            Planet("mars", 24*30*21, "planet"),
            Planet("pluto", 360*24*9.5, "planet?")
    ]


    gc = GroundControl(planets)

    _, _, report = gc.mission(rocket, rocket.get_crew(), gc.get_planets()[0])
    print(report)

main()
