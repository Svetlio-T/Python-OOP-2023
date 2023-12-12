from inher_need_for_speed_exer.car import Car


class FamilyCar(Car):

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
