class Exam:
    __slots__ = ['__group', '__examName', '__MAX_NUMBER_OF_ATTEMPTS']

    def __init__(self, group, examName):
        self.__group = group
        self.__examName = examName
        self.__MAX_NUMBER_OF_ATTEMPTS = 3


    def __str__(self):
        return 'Last exam [{}] in this group was passed: {}'.format(self.__examName, True if self.__group.attemptCount >= 3 else False)


    def checkGrades(self):
        for i in self.__group.studList:
            if i.grades[self.__examName] is None:
                continue
            i.grades[self.__examName].allowExam = (min(i.grades[self.__examName].grades) > 3)


    def examination(self):
        if self.__group.attemptCount >= self.__MAX_NUMBER_OF_ATTEMPTS:
            raise 'Exam for this group was ended'

        self.__group.attemptCount += 1
        is_last_attempt = self.__group.attemptCount == self.__MAX_NUMBER_OF_ATTEMPTS
        to_kick = []
        for i in self.__group.studList:
            this_exam = i.grades[self.__examName]
            if this_exam is None:
                continue
            if this_exam.allowExam is None:
                raise 'Group pass in the exam was not carry out'
            if this_exam.examGrade is None or this_exam.examGrade < 3:
                this_exam.examGrade = i.gradeKnowledge(is_last_attempt)

            if is_last_attempt and (i.grades.get(self.__examName).examGrade < 3 or i.grades.get(self.__examName).examGrade is None):
                to_kick.append(i.name)

        for student in to_kick:
            self.__group.removeStudentByName(student)