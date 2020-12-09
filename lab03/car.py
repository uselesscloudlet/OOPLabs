from details import Engine, Transmission, GasPedal, Wheels, Body

class Car():
    __slots__ = ['__engine', '__transmission', '__gasPedal', '__wheels', '__body']

    def __init__(self, engine = None, transmission = None, gasPedal = None, wheels = None, body = None):
        self.__engine = engine
        self.__transmission = transmission
        self.__gasPedal = gasPedal
        self.__wheels = wheels
        self.__body = body

    def __str__(self):
        return self.__checkReadiness()

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, transmission):
        self.__transmission = transmission

    @property
    def gasPedal(self):
        return self.__gasPedal

    @gasPedal.setter
    def gasPedal(self, gasPedal):
        self.__gasPedal = gasPedal

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        self.__wheels = wheels

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def __checkReadiness(self):
        if not isinstance(self.engine, Engine):
            raise 'This car has no Engine! Add it.'
        elif not isinstance(self.transmission, Transmission):
            raise 'This car has no Transmission! Add it.'
        elif not isinstance(self.gasPedal, GasPedal):
            raise 'This car has no Gas Pedal! Add it.'
        elif not isinstance(self.wheels, Wheels):
            raise 'This car has no Wheels! Add it.'
        elif not isinstance(self.body, Body):
            raise 'This car has no body! Add it.'
        else:
            return 'This car is ready to travel!'

    def simulate(self):
        pass