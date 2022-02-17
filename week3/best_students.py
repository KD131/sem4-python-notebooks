from typing import List

from student import Student


class NotEnoughStudentsException(Exception):
    pass

def three_closest_to_completion(students: List[Student]):
    if len(students) < 3:
        raise NotEnoughStudentsException
    return sorted(students, key=lambda s: s.get_total_progress(), reverse=True)[:3]
