from abc import ABC, abstractmethod
from enums import DetailType

class Detail(ABC):
    __slots__ = ['__weight']

    def __init__(self, weight):
        self.__weight = weight # вес

    def __str__(self):
        return 'This is Detail. Nobody knows what she does.'

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @abstractmethod
    def getDetailType(self):
        pass

    @abstractmethod
    def getDetailDescription(self):
        pass


class Engine(Detail):
    __slots__ = ['__power', '__torque', '__maxRevolutionsNumber']

    def __init__(self, power, torque, maxRevolutionsNumber, weight):
        self.__power = power # мощность
        self.__torque = torque # крутящий момент
        self.__maxRevolutionsNumber = maxRevolutionsNumber # макс число оборотов
        super().__init__(weight)

    def __str__(self):
        return self.getDetailDescription()

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def torque(self):
        return self.__torque

    @torque.setter
    def torque(self, torque):
        self.__torque = torque

    @property
    def maxRevolutionsNumber(self):
        return self.__maxRevolutionsNumber

    @maxRevolutionsNumber.setter
    def maxRevolutionsNumber(self, maxRevolutionsNumber):
        self.__maxRevolutionsNumber = maxRevolutionsNumber

    def getDetailType(self):
        return DetailType.ENGINE

    def getDetailDescription(self):
        return "This is {}. Options:\npower: {}\ntorque: {}\nmaxRevolutionNumber: {}\n".format(
            self.getDetailType,
            self.power,
            self.torque,
            self.maxRevolutionsNumber
            )


class Transmission(Detail):
    __slots__ = ['__transmissionType', '__gearsNumber']

    def __init__(self, transmissionType, gearsNumber, weight):
        self.__transmissionType = transmissionType # тип трансмиссии
        self.__gearsNumber = gearsNumber # кол-во передач
        super().__init__(weight)

    def __str__(self):
        return self.getDetailDescription()

    @property
    def transmissionType(self):
        return self.__transmissionType

    @transmissionType.setter
    def transmissionType(self, transmissionType):
        self.__transmissionType = transmissionType

    @property
    def gearsNumber(self):
        return self.__gearsNumber

    @gearsNumber.setter
    def gearsNumber(self, gearsNumber):
        self.__gearsNumber = gearsNumber

    def getDetailType(self):
        return DetailType.TRANSMISSION

    def getDetailDescription(self):
        return "This is {}. Options:\ntransmissionType: {}\ngearsNumber: {}\n".format(
            self.getDetailType,
            self.transmissionType,
            self.gearsNumber
            )


class GasPedal(Detail):

    def __init__(self):
        super().__init__(0)

    def __str__(self):
        return self.getDetailDescription()

    def getDetailType(self):
        return DetailType.GAS_PEDAL

    def getDetailDescription(self):
        return "This is {}. If is it, then it's already good.\n".format(
            self.getDetailType,
            )


class Wheels(Detail):
    __slots__ = ['__wheelWidth', '__wheelDiameter']

    def __init__(self, wheelWidth, wheelDiameter, weight):
        self.__wheelWidth = wheelWidth # ширина колеса
        self.__wheelDiameter = wheelDiameter # диаметр колеса
        super().__init__(weight)

    def __str__(self):
        return self.getDetailDescription()

    @property
    def wheelWidth(self):
        return self.__wheelWidth

    @wheelWidth.setter
    def wheelWidth(self, wheelWidth):
        self.__wheelWidth = wheelWidth

    @property
    def wheelDiameter(self):
        return self.__wheelDiameter

    @wheelDiameter.setter
    def wheelDiameter(self, wheelDiameter):
        self.__wheelDiameter = wheelDiameter

    def getDetailType(self):
        return DetailType.WHEELS

    def getDetailDescription(self):
        return "This is {}. Options:\nwheelWidth: {}\nwheelDiameter: {}\n".format(
            self.getDetailType,
            self.wheelWidth,
            self.wheelDiameter
            )


class Body(Detail):
    __slots__ = ['__type', '__color']

    def __init__(self, type, color, weight):
        self.__type = type # тип кузова
        self.__color = color # цвет кузова
        super().__init__(weight)

    def __str__(self):
        return self.getDetailDescription()

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def getDetailType(self):
        return DetailType.BODY
    
    def getDetailDescription(self):
        return "This is {}. Options:\ntype: {}\ncolor: {}\n".format(
            self.getDetailType,
            self.type,
            self.color
            )