from enums import Color, DetailType
from details import Engine, Transmission, GasPedal, Wheels, Body
from car import Car

engine = Engine(10, 10, 10, 15)
transmission = Transmission(10, 10, 10)
pedal = GasPedal()
wheels = Wheels(100, 4, 5)
body = Body(10, 10, 10)
car = Car(engine, transmission, pedal, wheels, body)
print(car)
