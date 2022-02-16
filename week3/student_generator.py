import csv
import platform
import random as rnd
from string import ascii_letters, ascii_uppercase
from typing import List

from course import Course
from data_sheet import DataSheet
from student import Student

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
        courses = generate_courses(4) # could also be randomised
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

def write_students_to_csv(students: List[Student]):
    # this capitalised type hint syntax is only for python v. 3.8 or earlier
    if platform.system() is "Windows":
        newline = ""
    else:
        newline = None

    with open("students.csv", "w", newline=newline) as file:
        # DictWriter is also really cool but perhaps not usuable here for three reasons.
        # 1. Objects are not dicts. I'd have to convert it first.
        # 2. The fields are spread out across inner objects as well.
        # 3. The headers requested for the CSV don't match the field names exactly.
        writer = csv.writer(file)
        writer.writerow(["stud_name", "course_name", "teacher", "gender", "ects", "classroom", "grade", "img_url"])
        for s in students:
            for c in s.data_sheet.courses:
                writer.writerow([s.name, c.name, c.teacher, s.gender, c.ects, c.classroom, c.grade, s.image_url])

# would make a lot of sense to also implement as a CLI program with args.
if __name__ == "__main__":
    write_students_to_csv(generate_students(4))
