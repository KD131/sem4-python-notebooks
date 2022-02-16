import csv

from course import Course
from data_sheet import DataSheet
from student import Student

c1 = Course("Mathematics", "A102", "OJ", 20, 3)
c2 = Course("English Literature", "C210", "JW", 10, 2)
c3 = Course("Chemistry", "B116", "EC", 20, 4)
c4 = Course("Gymnastics", "GYM", "TJ", 10)

s1 = Student("Michael", "male", DataSheet([c1, c2, c3, c4]), "...")
print(s1.data_sheet.get_grades_as_list())
print(s1.get_average_grade())

