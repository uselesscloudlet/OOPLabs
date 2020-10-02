class Grades:
    __slots__ = ['__grades', '__allowExam', '__examGrade']

    def __init__(self, grades):
        self.__grades = grades
        self.__allowExam = None
        self.__examGrade = None


    def __repr__(self):
        return '{} | AllowExam: {} | ExamGrade: {}'.format(self.grades, self.allowExam, self.examGrade)


    @property
    def grades(self):
        return self.__grades


    @grades.setter
    def grades(self, grades):
        self.__grades = grades


    @property
    def allowExam(self):
        return self.__allowExam


    @allowExam.setter
    def allowExam(self, allowExam):
        self.__allowExam = allowExam


    @property
    def examGrade(self):
        return self.__examGrade


    @examGrade.setter
    def examGrade(self, examGrade):
        self.__examGrade = examGrade
    