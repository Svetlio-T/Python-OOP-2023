from inher_need_for_speed_exer.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)