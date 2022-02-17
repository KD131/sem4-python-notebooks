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


students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        course = Course(row[1], row[5], row[2], int(row[4]), int(row[6]))
        student = next((s for s in students if s.image_url == row[7]), None) #using image_url as id because it's the closest we have to it.
        if student:
            student.data_sheet.courses.append(course)
        else:
            students.append(Student(row[0], row[3], DataSheet([course]), row[7]))

for s in students:
    print(f"{s.name}, URL: {s.image_url}, avg. grade: {s.get_average_grade()}")


print("\nSorting by avg. grade (desc.)\n=================")
students.sort(key=lambda s: s.get_average_grade(), reverse=True)

for s in students:
    print(f"{s.name}, URL: {s.image_url}, avg. grade: {s.get_average_grade()}")