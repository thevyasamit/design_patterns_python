'''
This code demonstrates factory method.
'''

from abc import ABC, abstractmethod


class CarShowroom(ABC):

    @abstractmethod
    def display_car():
        pass


class SUV(CarShowroom):

    def __init__(self, car_name: str) -> None:
        self.car_type = "SUV"
        self.car_name = car_name

    def display_car(self) -> None:
        print(f'my car type is {self.car_type} and my name is {self.car_name}')


class Sedan(CarShowroom):

    def __init__(self, car_name: str) -> None:
        self.car_type = "Sedan"
        self.car_name = car_name

    def display_car(self) -> None:
        print(f'my car type is {self.car_type} and my name is {self.car_name}')


class CarShowroomFactory(ABC):

    @abstractmethod
    def create_car_showroom(self, car_name: str) -> CarShowroom:
        pass


class SUVFactory(CarShowroomFactory):

    def create_car_showroom(self, car_name: str) -> CarShowroom:
        return SUV(car_name=car_name)


class SedanFactory(CarShowroomFactory):

    def create_car_showroom(self, car_name: str) -> CarShowroom:
        return Sedan(car_name=car_name)


SEDAN_CARS = ["Accord"]
SUV_CARS = ["CRV", "Rav4"]

REGISTRY = {
    SedanFactory: SEDAN_CARS,
    SUVFactory: SUV_CARS
}


'''
This function factory_call(), acting as the client, does not know about the
SUV or Sedan classes.
Instead, it uses factory methods provided by the SUVFactory and SedanFactory
to create objects.
'''


def factory_call() -> None:

    for factory, cars in REGISTRY.items():
        factory_class = factory()

        for car in cars:
            car_obj = factory_class.create_car_showroom(car)
            car_obj.display_car()


if __name__ == "__main__":

    factory_call()
