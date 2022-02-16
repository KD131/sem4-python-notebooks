import random as rnd
from string import ascii_letters, ascii_uppercase
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

course_names = ["Mathematics", "English Literature", "Chemistry", "Gymnastics", "History", "Biology", "Music", "Physics", "Social Sciences"]
fnames_male = ["Michael", "Matthew", "Robert", "Richard", "Hans", "William", "George", "David", "Adam"]
fnames_female = ["Emma", "Alice", "Sophie", "Camilla", "Eva", "Amy", "Clara", "Theresa", "Anne"]
last_names = ["Hansen", "Thompson", "Jensen", "Sarif", "Turner", "Portman", "Robertson", "Watson", "Murduck", "Michael", "Cassidy", "Pond", "Pattinson", "Burr", "Vreeland", "Shakespeare", "Longdon"]
genders = ["male", "female"]

def generate_students(num: int):
    students = []
    for i in range(num):
        gender = rnd.choice(genders)
        if gender is "male":
            fname = rnd.choice(fnames_male)
        elif gender is "female":
            fname = rnd.choice(fnames_female)
        lname = rnd.choice(last_names)
        courses = generate_courses(4)
        image_url = "".join(rnd.choices(ascii_letters, k=8))
        students.append(Student(f"{fname} {lname}", gender, DataSheet(courses), image_url))
    return students
        
def generate_courses(num: int):
    courses = []
    names = rnd.sample(course_names, num)
    for name in names:
        classroom = rnd.choice(["A", "B", "C", "D", "E", "F"]) + str(rnd.randint(101, 399))
        teacher = "".join(rnd.choices(ascii_uppercase, k=2))
        ects = rnd.choice([10, 15, 20, 30])
        grade = rnd.randint(1, 5)
        courses.append(Course(name, classroom, teacher, ects, grade))
    return courses

print(generate_students(4))
