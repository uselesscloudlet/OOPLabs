from grades import Grades
from random import randint
from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    __slots__ = ['__name', '__grades']

    def __init__(self, name, grades):
        self.__name = name
        self.__grades = dict()
        for grade in grades:
            subjectName = grade[0]
            self.__grades[subjectName] = Grades(grade[1])

    
    def __str__(self):
        return '\n{} named {} with grades: \n{}'.format(self.status, self.name, "".join(g + ": " + str(self.grades[g]) + "\n" for g in self.grades))


    def addSubjectAndGrade(self, subjectName, grades):
        self.__grades[subjectName] = Grades(grades)


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
        AbstractStudent.__init__(self, name, map(lambda g: (g[0], [5] * len(g[1])), grades))


    @property
    def status(self):
        return 'Nerd Student'


    def gradeKnowledge(self, isLastAttempt = False):
        return randint(4, 5)