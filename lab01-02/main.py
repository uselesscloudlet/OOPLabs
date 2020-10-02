from students import AbstractStudent, DefaultStudent, MemberOfStudentCouncil, NerdStudent
from group import Group
from exam import Exam
from grades import Grades


stud1 = DefaultStudent('A A A', [('Math', [4, 4, 4])])
stud1.addSubjectAndGrade('Physics', [3, 4, 3])
stud2 = DefaultStudent('B B B', [('Math', [2, 2, 2]), ('Physics', [5, 5, 5])])
stud3 = NerdStudent('CCC', [('Math', [2, 2, 2]), ('Physics', [2, 2, 2])])
group = Group('8888', 20, [stud1, stud2, stud3])
exam = Exam(group, 'Math')
exam1 = Exam(group, 'Physics')
exam.checkGrades()
exam.examination()
exam.examination()
exam.examination()
print(group)