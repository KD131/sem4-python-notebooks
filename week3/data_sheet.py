from notebooks.my_notebooks.week3.course import Course


class DataSheet:
    def __init__(self, courses: list[Course]):
        self.courses = courses
    
    def get_grades_as_list(self):
        return [c.grade for c in self.courses]