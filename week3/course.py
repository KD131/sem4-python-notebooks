class Course:
    # Python for VS Code breaks syntax highlighting when using function return type arrows
    def __init__(self, name, classroom, teacher, ects, grade=0) -> None:
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def __repr__(self) -> str:
        return "Course(%r, %r, %r, %r, %r)" % (self.name, self.classroom, self.teacher, self.ects, self.grade)