import unittest

from astronaut import Astronaut
from rocket import Rocket
from ground_control import GroundControl
from planet import Planet


class Tests(unittest.TestCase):

    planets = [
            Planet("moon", 24*3, "moon"),
            Planet("mars", 24*30*21, "planet"),
            Planet("pluto", 360*24*9.5, "planet?")
    ]

    def test_astronaut(self):
        neil = Astronaut("Neil", 10)

        # Do not change
        self.assertEqual(neil.get_name(), "Neil")
        self.assertEqual(neil.get_work_unit(), 10)
        self.assertEqual(neil.work(2), 20)
        ######

    def test_rocket(self):
        rocket = Rocket()

        rocket.set_name("Soyuz")
        rocket.set_fuel(100)
        rocket.set_food(100)
        crew = [Astronaut("Neil", 10)]
        rocket.set_crew(crew)

        # Do not change
        self.assertEqual(rocket.get_name(), "Soyuz")
        self.assertEqual(rocket.get_fuel(), 100)
        self.assertEqual(rocket.get_food(), 100)
        self.assertListEqual(rocket.get_crew(), crew)
        ######

    def test_rocket_no_fuel(self):
        rocket = Rocket()

        rocket.set_name("Soyuz")
        rocket.set_fuel(0)
        rocket.set_food(100)
        crew = [Astronaut("Neil", 10)]
        rocket.set_crew(crew)

        ground_control = GroundControl(self.planets)

        res, work, report = ground_control.mission(rocket, crew, ground_control.get_planets()[0])

        # Do not change
        self.assertEqual(res, False)
        self.assertEqual(work, 0)
        self.assertEqual(report, "The travel has failed.\n1 crew members.\nRocket has 0 fuel left.\nCrew has worked 0 units.")
        ####

    def test_no_crew_members(self):
        rocket = Rocket()

        rocket.set_name("Soyuz")
        rocket.set_fuel(100)
        rocket.set_food(100)
        rocket.set_crew([])

        ground_control = GroundControl(self.planets)

        res, work, report = ground_control.mission(rocket, [], ground_control.get_planets()[0])

        # Do not change
        self.assertEqual(res, False)
        self.assertEqual(work, 0)
        self.assertEqual(report, "The travel has failed.\n0 crew members.\nRocket has 100 fuel left.\nCrew has worked 0 units.")
        ####

    def test_unknown_planet(self):
        rocket = Rocket()

        rocket.set_name("Soyuz")
        rocket.set_fuel(100)
        rocket.set_food(100)
        crew = [Astronaut("Neil", 10)]
        rocket.set_crew(crew)

        ground_control = GroundControl(self.planets)

        res, work, report = ground_control.mission(rocket, crew, Planet("uranus", 1, "planet"))

        # Do not change
        self.assertEqual(res, False)
        self.assertEqual(work, 0)
        self.assertEqual(report, "The travel has failed.\n1 crew members.\nRocket has 100 fuel left.\nCrew has worked 0 units.")
        ####


if __name__ == '__main__':
    unittest.main()
