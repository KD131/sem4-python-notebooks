from typing import List
from data_sheet import DataSheet

from student import Student
from student_generator import read_students_from_csv, write_students_to_csv


class NotEnoughStudentsException(Exception):
    pass

def three_closest_to_completion(students: List[Student]):
    if len(students) < 3:
        raise NotEnoughStudentsException
    return sorted(students, key=lambda s: s.get_total_progress(), reverse=True)[:3]

if __name__ == "__main__":
    # test to trigger the exception
    students = [Student("test", "test", DataSheet([]), "test")]
    students = read_students_from_csv("students.csv")
    try:
        furthest = three_closest_to_completion(students)
        write_students_to_csv(furthest, "furthest_students.csv")
    except NotEnoughStudentsException:
        print("Need at least 3 students, mate")
