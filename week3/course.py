class Course:
    def __init__(self, name, classroom, teacher, ects, grade=0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def __repr__(self) -> str:
        return "Course(%r, %r, %r, %r, %r)" % (self.name, self.classroom, self.teacher, self.ects, self.grade)