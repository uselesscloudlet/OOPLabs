from students import AbstractStudent, DefaultStudent, MemberOfStudentCouncil, NerdStudent
from group import Group
from exam import Exam
from grades import Grades


stud1 = DefaultStudent('A A A', Grades('Math', [4, 4, 4]))
stud1.addSubjectAndGrade(Grades('Physics', [3, 4, 3]))
stud2 = DefaultStudent('B B B', Grades('Math', [2, 2, 2]))
stud2.addSubjectAndGrade(Grades('Physics', [5, 5, 5]))
group = Group('8888', 20, [stud1, stud2])
exam = Exam(group, 'Math')
exam1 = Exam(group, 'Physics')
exam.checkGrades()
exam.examination()
# print(group)