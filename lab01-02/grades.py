class Grades:
    __slots__ = ['__grades']

    def __init__(self, grades):
        self.__grades = {
            "grades": grades,
            "allowExam": None,
            "examGrade": None
        }
         # dict(subjectName=grades) не работает. Выдает вариант в виде 'subjectName': [...]


    def __repr__(self):
        return '{} | AllowExam: {} | ExamGrade: {}'.format(self.grades, self.allowExam, self.examGrade)


    @property
    def grades(self):
        return self.__grades["grades"]


    @grades.setter
    def grades(self, grades):
        self.__grades["grades"] = grades


    @property
    def allowExam(self):
        return self.__grades["allowExam"]


    @allowExam.setter
    def allowExam(self, allowExam):
        self.__grades["allowExam"] = allowExam


    @property
    def examGrade(self):
        return self.__grades["examGrade"]


    @examGrade.setter
    def examGrade(self, examGrade):
        self.__grades["examGrade"] = examGrade
    