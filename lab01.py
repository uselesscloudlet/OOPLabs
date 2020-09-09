class Student:
    def __init__(self, name, grades):
        self.__name = name
        if not grades:
            self.__grades = []
        else:
            self.__grades = grades
    

    def __str__(self):
        return 'Student named {} with grades: {}.'.format(self.__name, self.__grades)

    
    def setName(self, name):
        self.__name = name

    
    def getName(self):
        return self.__name


    def setGrades(self, grades):
        self.__grades = grades


    def getGrades(self):
        return self.__grades

    
class Group:
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


# Tests
group8091 = Group('8091', 20, None)
group9091 = Group('9091', 10, None)

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