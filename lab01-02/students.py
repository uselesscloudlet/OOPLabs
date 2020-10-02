from random import randint
from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    __slots__ = ['__name', '__grades', '__allowExam', '__examGrade']

    def __init__(self, name, grades):
        self.__name = name
        self.__allowExam = None
        self.__examGrade = None
        if not grades:
            self.__grades = []
        else:
            self.__grades = grades

    
    def __str__(self):
        return '{} named {} with grades: {} and exam grade {}.'.format(self.status, self.name, self.grades, self.examGrade)


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def grades(self):
        return self.__grades


    @grades.setter
    def grades(self, grades):
        self.__grades = grades


    @property
    def allowExam(self):
        return self.__allowExam


    @allowExam.setter
    def allowExam(self, allowExam):
        self.__allowExam = allowExam


    @property
    def examGrade(self):
        return self.__examGrade


    @examGrade.setter
    def examGrade(self, examGrade):
        self.__examGrade = examGrade


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