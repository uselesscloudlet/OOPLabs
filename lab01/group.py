class Group:
    __slots__ = ['__groupName', '__maxGroupSize', '__studentsList']

    def __init__(self, groupName, maxGroupSize, studentList):
        self.__groupName = groupName
        self.__maxGroupSize = maxGroupSize
        if not studentList:
            self.__studentsList = []
        else:
            self.__studentsList = studentList
    

    def __str__(self):
        return self.getStudentsList()


    def setGroupName(self, groupName = ''):
        self.__groupName = groupName


    def getGroupName(self):
        return self.__groupName


    def addStudent(self, student):
        if len(self.__studentsList) < self.__maxGroupSize:
            self.__studentsList.append(student)
        else:
            raise('Failed to add student. The group is overcrowded.')
    

    def removeStudentByName(self, name = ''):
        checkStudent = False
        for i in self.__studentsList:
            if i.getName() == name:
                checkStudent = True
                self.__studentsList.remove(i)
        if not checkStudent:
            raise('Student with name {} not found.'.format(name))


    def getStudentsList(self):
        if len(self.__studentsList) == 0:
            return 'List of students {} group is empty.\n'.format(self.getGroupName())
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: stud.getName())
            message += ('List of students {} group:\n'.format(self.getGroupName()))
            for i in self.__studentsList:
                message += '{} - {}\n'.format(i.getName(), i.getGrades())
            return message


    def getStudentListSortedByGrades(self):
        if len(self.__studentsList) == 0:
            return('List of students {} group is empty.\n'.format(self.getGroupName()))
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: sum(stud.getGrades()) / len(stud.getGrades()), reverse=True)
            message += ('List of students {} group:\n'.format(self.getGroupName()))
            for i in self.__studentsList:
                message += '{} - {}\n'.format(i.getName(), i.getGrades())
            return message