from abc import ABC, abstractmethod

class AbstractStudent(ABC):
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


    @abstractmethod
    def getStatus(self):
        pass


class DefaultStudent(AbstractStudent):

    def getStatus(self):
        return 'Default Student'


class MemberOfStudentCouncil(DefaultStudent):

    def getStatus(self):
        return 'Member of Student Council'

# class NerdStudent(AbstractStudent):