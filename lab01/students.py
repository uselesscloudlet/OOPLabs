from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    __slots__ = []

    @abstractmethod
    def __init__(self, cls):
        raise TypeError(
                "TypeError: Can't instantiate abstract class {name} directly".format(name=cls.__name__)
            )

    
    @abstractmethod
    def setName(self, name):
        pass

    
    @abstractmethod
    def getName(self):
        pass


    @abstractmethod
    def setGrades(self, grades):
        pass


    @abstractmethod
    def getGrades(self):
        pass


    @abstractmethod
    def getStatus(self):
        pass


class DefaultStudent(AbstractStudent):
    __slots__ = ['__name', '__grades']

    def __init__(self, name, grades):
        self.__name = name
        if not grades:
            self.__grades = []
        else:
            self.__grades = grades
    

    def __str__(self):
        return '{} named {} with grades: {}.'.format(self.getStatus(), self.getName(), self.getGrades())

    
    def setName(self, name):
        self.__name = name

    
    def getName(self):
        return self.__name


    def setGrades(self, grades):
        self.__grades = grades


    def getGrades(self):
        return self.__grades


    def getStatus(self):
        return 'Default Student'


class MemberOfStudentCouncil(DefaultStudent):
    __slots__ = ['__name', '__grades']


    def getStatus(self):
        return 'Member of Student Council'

    def __str__(self):
        return '{} named {} with grades: {}.'.format(self.getStatus(), self.getName(), self.getGrades())