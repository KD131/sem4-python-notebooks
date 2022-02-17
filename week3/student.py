from platform import release
from statistics import mean
from typing import List

from data_sheet import DataSheet

# Python for VS Code breaks syntax highlighting when using function return type arrows

class NotEnoughStudentsException(Exception):
    pass

class Student:
    def __init__(self, name, gender, data_sheet: DataSheet, image_url) -> None:
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def __repr__(self) -> str:
        return "Student(%r, %r, %r, %r)" % (self.name, self. gender, self.data_sheet, self.image_url)

    def get_average_grade(self):
        return mean(self.data_sheet.get_grades_as_list())

    def get_total_progress(self):
        """Returns percentage as number"""
        return (sum([c.ects for c in self.data_sheet.courses])/150)*100

    @staticmethod
    def three_closest_to_completion(students: List["Student"]):
        if len(students) < 3:
            raise NotEnoughStudentsException
        return sorted(students, key=lambda s: s.get_total_progress(), reverse=True)[:3]
