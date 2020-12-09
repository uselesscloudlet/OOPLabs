from threading import Timer
from enum import Enum, auto


class OperatorType(Enum):
    PAYTAX = auto()
    OPENBIS = auto()
    ASKQUESTION = auto()


timeDict = {OperatorType.PAYTAX: 10,
            OperatorType.OPENBIS: 30,
            OperatorType.ASKQUESTION: 5}


class Operator():
    __slots__ = ['__name', '__types', '__isFree',
                 '__queue', '__timer', '__clientsNumber']

    def __init__(self, name, types, queue):
        self.__name = name
        self.__types = types
        self.__isFree = True
        self.__queue = queue
        self.__clientsNumber = 0
        self.__queue.addOperator(self)

    def __str__(self):
        return 'Operator is {}'.format("working" if not self.__isFree else "finished")

    def __del__(self):
        print('{} processed {} clients'.format(
            self.__name, self.__clientsNumber))

    @property
    def types(self):
        return self.__types

    @property
    def isFree(self):
        return self.__isFree

    @property
    def clientsNumber(self):
        return self.__clientsNumber

    def workWithVisitor(self, visitor):
        self.__isFree = False
        self.__clientsNumber += 1
        timer = Timer(timeDict[visitor.type], self.__finishWithVisitor)
        timer.start()

    def __finishWithVisitor(self):
        self.__isFree = True
        self.__queue.findVisitorForOperator(self)