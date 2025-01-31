class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def strat(self):
        print(f'{self.brand} {self.model} started.')
    
    def stop(self):
        print(f'{self.brand} {self.model} stopped.')


class Car(Vehicle):

    def  __init__(self, brand, model, year,door_number,wheel_number):
        super().__init__(brand, model, year)
        self.doornumber=door_number
        self.wheelnumber=wheel_number

class Bike(Vehicle):
    def __init__(self, brand, model, year,engine_capacity):
        super().__init__(brand, model, year)
        self.enginecapacity=engine_capacity


car=Car('Toyota','Corolla',2019,4,4)
car.strat()
car.stop()
bike=Bike('Yamaha','FZ',2018,150)
bike.strat()
bike.stop()

print(car.__dict__)
print(bike.__dict__)