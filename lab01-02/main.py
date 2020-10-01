from students import AbstractStudent, DefaultStudent, MemberOfStudentCouncil, NerdStudent
from group import Group
from exam import Exam

#1
stud1 = DefaultStudent('A A A', [2, 3, 4])
stud2 = DefaultStudent('B B B', [3, 3, 4])
stud3 = DefaultStudent('C C C', [4, 4, 5])
stud4 = DefaultStudent('D D D', [3, 4, 4])

group = Group('8091', 20, [stud1, stud2, stud3, stud4])
exam = Exam(group)
exam.checkGrades()
print(exam)
exam.examination()
exam.examination()
exam.examination()
print(group.getStudentsList())
print(exam)

#2
stud1 = NerdStudent('A A A', [2, 3, 4])
stud2 = MemberOfStudentCouncil('B B B', [3, 3, 4])
stud3 = DefaultStudent('C C C', [4, 4, 5])
stud4 = DefaultStudent('D D D', [3, 4, 4])

group = Group('8091', 20, [stud1, stud2, stud3, stud4])
exam = Exam(group)
exam.checkGrades()
exam.examination()
exam.examination()
exam.examination()
print(group.getStudentsList())