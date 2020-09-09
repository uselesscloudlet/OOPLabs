class Student:
    def __init__(self, name = ''):
        self._name = name
    

    def __str__(self):
        return 'Student named {}'.format(self._name)


    def setName(self, name):
        self._name = name


    def getName(self):
        return self._name

    
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
        if (len(self.__studentsList) < self.__maxGroupSize):
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
        if (len(self.__studentsList) == 0):
            return('List of students {} group is empty.\n'.format(self.__groupName))
        else:
            message = ''

            self.__studentsList = sorted(self.__studentsList, key=lambda stud: stud._name)
            message += ('List of students {} group:\n'.format(self.__groupName))
            for i in self.__studentsList:
                message += i.getName() + '\n'
            return message


# Tests
group8091 = Group('8091', 20)
group9091 = Group('9091', 10)
group0091 = Group('0091', 10)

student1 = Student('wee')
student2 = Student('aaa')
print(student1)
group8091.addStudent(student1)
group8091.addStudent(student2)
group9091.addStudent(student1)

print(group8091)
group8091.removeStudentByName('wee')
group8091.removeStudentByName('aaa')
print(group8091)
print(group9091)
print(group0091)
print(group0091)