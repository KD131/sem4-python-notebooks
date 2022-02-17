from course import Course
from data_sheet import DataSheet
from student_generator import read_students_from_csv
from student import Student

c1 = Course("Mathematics", "A102", "OJ", 20, 3)
c2 = Course("English Literature", "C210", "JW", 10, 2)
c3 = Course("Chemistry", "B116", "EC", 20, 4)
c4 = Course("Gymnastics", "GYM", "TJ", 10)

s1 = Student("Michael", "male", DataSheet([c1, c2, c3, c4]), "...")
print(s1.data_sheet.get_grades_as_list())
print(s1.get_average_grade())


students = read_students_from_csv()

for s in students:
    print(f"{s.name}, URL: {s.image_url}, avg. grade: {s.get_average_grade()}")


print("\nSorting by avg. grade (desc.)\n=================")
students.sort(key=lambda s: s.get_average_grade(), reverse=True)

for s in students:
    print(f"{s.name}, URL: {s.image_url}, avg. grade: {s.get_average_grade()}")

print("\n% progress\n=================")
print(f"Test Student s1 ({s1.name}): {s1.get_total_progress()}% of the way")

for s in students:
    print(f"({s.name}): {s.get_total_progress()}% of the way")

print(next(iter(s1.data_sheet)))
for c in s1.data_sheet:
    print(c)

for s in Student.three_closest_to_completion(students):
    print(s.name, s.get_total_progress())
