from students import AbstractStudent, DefaultStudent, MemberOfStudentCouncil, NerdStudent
from group import Group
from exam import Exam

import unittest


group = Group('8091', 20, [])

for i in range(3):
    group.addStudent(DefaultStudent(i, [1, 1, 1]))
exam = Exam(group)
print(group.getStudentsList())
exam.checkGrades()
print(group.getStudentsList())
exam.examination()
exam.examination()
exam.examination()
print(group.getStudentsList())
