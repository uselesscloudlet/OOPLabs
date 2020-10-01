class Group:
    __slots__ = ['__groupName', '__maxGroupSize', '__studentsList', '__attemptCount']

    def __init__(self, groupName, maxGroupSize, studentList):
        self.__groupName = groupName
        self.__maxGroupSize = maxGroupSize
        self.__attemptCount = 0
        if not studentList:
            self.__studentsList = []
        else:
            self.__studentsList = studentList
    

    def __str__(self):
        return self.getStudentsList()


    @property
    def groupName(self):
        return self.__groupName


    @groupName.setter
    def groupName(self, groupName):
        self.__groupName = groupName


    @property
    def studList(self):
        return self.__studentsList


    @property
    def attemptCount(self):
        return self.__attemptCount

    
    @attemptCount.setter
    def attemptCount(self, number):
        self.__attemptCount = number


    def getStudentsList(self):
        if len(self.__studentsList) == 0:
            return 'List of students {} group is empty.\n'.format(self.groupName)
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: stud.name)
            message += ('List of students {} group:\n'.format(self.groupName))
            for i in self.__studentsList:
                message += '[{}] {} - {}, Allow Exam: {} | Attempt: {}, Exam Success: {}, Exam Grade: {}\n'.format(
                    i.status, i.name, i.grades, i.allowExam, self.attemptCount,
                    True if (i.examGrade is not None) and (i.examGrade > 3) else False, i.examGrade)
            return message


    def getStudentListSortedByGrades(self):
        if len(self.__studentsList) == 0:
            return('List of students {} group is empty.\n'.format(self.groupName))
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: sum(stud.grades) / len(stud.grades), reverse=True)
            message += ('List of students {} group:\n'.format(self.groupName))
            for i in self.__studentsList:
                message += '[{}] {} - {}, Allow Exam: {} | Attempt: {}, Exam Success: {}, Exam Grade: {}\n'.format(
                    i.status, i.name, i.grades, i.allowExam,self.attemptCount,
                    True if i.allowExam is not None and i.examGrade > 3 else False, i.examGrade)
            return message
    

    

    def addStudent(self, student):
        if len(self.__studentsList) < self.__maxGroupSize:
            self.__studentsList.append(student)
        else:
            raise('Failed to add student. The group is overcrowded.')
    

    def removeStudentByName(self, name):
        checkStudent = False
        for i in self.__studentsList:
            if i.name == name:
                checkStudent = True
                self.__studentsList.remove(i)
        if not checkStudent:
            raise('Student with name {} not found.'.format(name))