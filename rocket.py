class Rocket():

    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_fuel(self):
        return self.fuel

    def set_crew(self, crew):
        self.crew = crew

    def get_crew(self):
        return self.crew

    def set_food(self, food):
        self.food = food

    def get_food(self):
        return self.food

    def launch(self):
        if self.fuel > 10:
            self.fuel -= 10

    @staticmethod
    def fuel_per_hour(rocket):
        if rocket.name.lower() == "soyuz":
            return 10
        if rocket.name.lower() == "n1":
            return 10
        if rocket.name.lower() == "apollo":
            return 8
        if rocket.name.lower() == "atlas":
            return 9

    @staticmethod
    def food_per_day(rocket):
        return len(rocket.get_crew()) * 3

    @staticmethod
    def travel(rocket, destination):
        rocket.launch()
        time = destination[1]
        consume = Rocket.fuel_per_hour(rocket)
        total = time * consume

        food_needed = Rocket.food_per_day(rocket) * time/24

        total_work = 0
        if rocket.get_fuel() >= total and food_needed <= rocket.get_food():
            for crew in rocket.get_crew():
                total_work += crew.work(time)
            return True, total_work
        else:
            return False, total_work
