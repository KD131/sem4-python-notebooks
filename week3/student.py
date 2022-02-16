from statistics import mean

from data_sheet import DataSheet


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
