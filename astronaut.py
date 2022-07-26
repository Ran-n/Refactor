class Astronaut():

    def __init__(self, name, work_unit):
        self.name = name
        self.work_unit = work_unit

    def work(self, time):
        return self.work_unit * time

    @staticmethod
    def board_rocket(rocket, astronaut):
        rocket.get_crew().append(astronaut)
        astronaut.on_rocket = True
