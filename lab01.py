class Student:
    def __init__(self, name = '', group = 0):
        self._name = name
    

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
            print('List of students {} group is empty.'.format(self.__groupName))
        else:
            self.__studentsList = sorted(self.__studentsList, key=lambda stud: stud._name)
            print('List of students {} group:'.format(self.__groupName))
            for i in self.__studentsList:
                print('{}'.format(i.getName()))


# Tests
group8091 = Group('8091', 20)
group9091 = Group('9091', 10)
group0091 = Group('0091', 10)

student1 = Student('wee')
student2 = Student('aaa')

group8091.addStudent(student1)
group8091.addStudent(student2)
group9091.addStudent(student1)

group8091.getStudentsList()
group8091.removeStudentByName('wee')
group8091.removeStudentByName('aaa')
group8091.getStudentsList()
group9091.getStudentsList()
group0091.getStudentsList()