from students import AbstractStudent, DefaultStudent, MemberOfStudentCouncil
from group import Group


student = DefaultStudent('Mikhailov Aleksey Georgievich', [5, 5, 5])
stud1 = MemberOfStudentCouncil('Nikolaev Dmitry Alekseevich', [4, 4, 4])
print(student)
print(stud1)
absStd = AbstractStudent('Wee Wee', [1, 1, 1])
print(absStd)