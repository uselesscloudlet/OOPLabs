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
            for j in i.grades:
                if j.grades.get(self.__examName) == None:
                    continue
                if min(j.grades.get(self.__examName)) < 3:
                    j.allowExam = False
                else:
                    j.allowExam = True


    def examination(self):
        for i in self.__group.studList:
            for j in i.grades:
                if j.allowExam is None:
                    raise 'Group pass in the exam was not carry out'
                # if j.grades.get(self.__examName) == None:
                #     continue
                # if min(j.grades.get(self.__examName)) < 3:
                #     j.allowExam = False
                # else:
                #     j.allowExam = True
        

        if not self.__group.studList or self.__group.studList[0].allowExam == None:
            raise 'Group pass in the exam was not carry out'
        if self.__group.attemptCount >= self.__MAX_NUMBER_OF_ATTEMPTS:
            raise 'Exam for this group was ended'
        self.__group.attemptCount += 1
        to_kick = []

        for i in filter(lambda s: (s.grades.get(self.__examName).examGrade is None 
                                   or s.grades.get(self.__examName).examGrade < 3)
                                   and s.grades.get(self.__examName).allowExam,
                                   self.__group.studList):
            is_last_attempt = self.__group.attemptCount == self.__MAX_NUMBER_OF_ATTEMPTS
            i.grades.get(self.__examName).examGrade = i.gradeKnowledge(is_last_attempt)
                
            if is_last_attempt and (i.grades.get(self.__examName).examGrade < 3 or i.grades.get(self.__examName).examGrade is None):
                to_kick.append(i.name)

        for student in to_kick:
            self.__group.removeStudentByName(student)