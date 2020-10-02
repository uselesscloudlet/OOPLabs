class Exam:
    __slots__ = ['__group', '__MAX_NUMBER_OF_ATTEMPTS']

    def __init__(self, group):
        self.__group = group
        self.__MAX_NUMBER_OF_ATTEMPTS = 3


    def __str__(self):
        return 'Last exam in this group was passed: {}'.format(True if self.__group.attemptCount >= 3 else False)


    def checkGrades(self):
        for i in self.__group.studList:
            if min(i.grades) < 3:
                i.allowExam = False
            else:
                i.allowExam = True


    def examination(self):
        if not self.__group.studList or self.__group.studList[0].allowExam == None:
            raise 'Group pass in the exam was not carry out'
        if self.__group.attemptCount >= self.__MAX_NUMBER_OF_ATTEMPTS:
            raise 'Exam for this group was ended'
        self.__group.attemptCount += 1
        to_kick = []

        for i in filter(lambda s: (s.examGrade is None or s.examGrade < 3) and s.allowExam, self.__group.studList):
            is_last_attempt = self.__group.attemptCount == self.__MAX_NUMBER_OF_ATTEMPTS
            i.examGrade = i.gradeKnowledge(is_last_attempt)
                
            if is_last_attempt and (i.examGrade < 3 or i.examGrade is None):
                to_kick.append(i.name)

        for student in to_kick:
            self.__group.removeStudentByName(student)