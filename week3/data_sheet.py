from course import Course
from typing import List

# this capitalised type hint syntax is only for python v. 3.8 or earlier
# Python for VS Code breaks syntax highlighting when using function return type arrows


class DataSheet:
    def __init__(self, courses: List[Course]) -> None:
        self.courses = courses

    def __repr__(self) -> str:
        return "DataSheet(%r)" % (self.courses)
    
    def get_grades_as_list(self):
        return [c.grade for c in self.courses]