from random import randint

class Exam:
    __slots__ = ['__group', '__MAX_NUMBER_OF_ATTEMPTS']

    def __init__(self, group):
        self.__group = group
        self.__MAX_NUMBER_OF_ATTEMPTS = 3

    def checkGrades(self):
        for i in self.__group.studList:
            if min(i.grades) < self.__MAX_NUMBER_OF_ATTEMPTS:
                i.allowExam = False
            else:
                i.allowExam = True

    def examination(self):
        if self.__group.studList[0].allowExam == None:
            raise 'Group pass in the exam was not carry out'
        if self.__group.attemptCount == self.__MAX_NUMBER_OF_ATTEMPTS:
            raise 'Exam for this group was ended'
        for i in filter(lambda s: (s.examGrade is None or s.examGrade < 3) and s.allowExam, self.__group.studList):
            if i.status == 'Nerd Student':
                i.examGrade = 5
            elif i.status == 'Member of Student Council':
                if i.attemptCount != self.__MAX_NUMBER_OF_ATTEMPTS:
                    i.examGrade = randint(1, 5)
                else:
                    i.examGrade = 3
            elif i.status == 'Default Student':
                i.examGrade = randint(1, 5)
        self.__group.attemptCount = self.__group.attemptCount + 1