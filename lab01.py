class Student:
    def __init__(self, name = '', grades = False):
        self._name = name
        if not grades:
            self._grades = []
        else:
            self._grades = grades
    

    def __str__(self):
        return 'Student named {}'.format(self._name)


    def setName(self, name):
        self._name = name


    def getName(self):
        return self._name


    def setGrades(self, grades):
        self._grades = grades


    def getGrades(self):
        return self._grades

    
class Group:
    def __init__(self, groupName = '', maxGroupSize = 0, studentList = False):
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
            print('Failed to add student. The group is overcrowded.')
    

    def removeStudentByName(self, name = ''):
        checkStudent = False
        for i in self.__studentsList:
            if i.getName() == name:
                checkStudent = True
                self.__studentsList.remove(i)
        if not checkStudent:
            print('Student with name {} not found.'.format(name))


    def getStudentsList(self):
        if len(self.__studentsList) == 0:
            return('List of students {} group is empty.\n'.format(self.__groupName))
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: stud.getName())
            message += ('List of students {} group:\n'.format(self.__groupName))
            for i in self.__studentsList:
                message += '{} - {}\n'.format(i.getName(), i.getGrades())
            return message


    def getStudentListSortedByGrades(self):
        if len(self.__studentsList) == 0:
            return('List of students {} group is empty.\n'.format(self.__groupName))
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: sum(stud.getGrades()) / len(stud.getGrades()), reverse=True)
            message += ('List of students {} group:\n'.format(self.__groupName))
            for i in self.__studentsList:
                message += '{} - {}\n'.format(i.getName(), i.getGrades())
            return message


# Tests
group8091 = Group('8091', 20)
group9091 = Group('9091', 10)

student1 = Student('wee', [5, 5, 5])
student2 = Student('aaa', [4, 3, 4])
student3 = Student('rrr', [4, 4, 4])
group8091.addStudent(student1)
group8091.addStudent(student2)
group8091.addStudent(student3)

print(group8091.getStudentListSortedByGrades())
print(group8091)
# print(group8091)
# group8091.removeStudentByName('wee')
# group8091.removeStudentByName('aaa')
# print(group8091)
# print(group9091)