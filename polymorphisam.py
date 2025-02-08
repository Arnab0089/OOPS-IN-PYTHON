class Car:
    def __init__(self,brand,model,year,door_number,wheel_number):
        self.brand=brand
        self.model=model
        self.year=year
        self.doornumber=door_number
        self.wheelnumber=wheel_number
    
    def strat(self):
        print(f'{self.brand} {self.model} started.')

    def stop(self):
        print(f'{self.brand} {self.model} stopped.')


class Bike:
    def __init__(self,brand,model,year,engine_capacity):
        self.brand=brand
        self.model=model
        self.year=year
        self.enginecapacity=engine_capacity

    def strat(self):
        print(f'{self.brand} {self.model} started.')

    def stop(self):
        print(f'{self.brand} {self.model} stopped.')