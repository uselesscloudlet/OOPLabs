from random import randint
from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    __slots__ = ['__name', '__grades']

    def __init__(self, name, grades):
        self.__name = name
        self.__grades = [grades]

    
    def __str__(self):
        return '{} named {} with grades: {}.\n'.format(self.status, self.name, self.grades)


    def addSubjectAndGrade(self, grade):
        self.__grades.append(grade)

    @property
    def grades(self):
        return self.__grades


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def gradeKnowledge(self, isLastAttempt = False):
        pass


class DefaultStudent(AbstractStudent):

    @property
    def status(self):
        return 'Default Student'

    def gradeKnowledge(self, isLastAttempt = False):
        return randint(1, 5)


class MemberOfStudentCouncil(DefaultStudent):

    @property
    def status(self):
        return 'Member of Student Council'

    def gradeKnowledge(self, isLastAttempt = False):
        return (3 if isLastAttempt else super().gradeKnowledge())

class NerdStudent(AbstractStudent):

    def __init__(self, name, grades):
        AbstractStudent.__init__(self, name, grades=[5] * len(grades))


    @property
    def status(self):
        return 'Nerd Student'

    def gradeKnowledge(self, isLastAttempt = False):
        return randint(4, 5)