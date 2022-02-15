import string

class InvalidArgumentException(Exception):
    pass

class Person:
    def __init__(self, name):
        self.validate_name(name)
        self.name = name

    def validate_name(self, name):
        if not name.istitle():
            raise InvalidArgumentException("Name must be title case, i.e. first letter of a word is upper case", name)
        for c in name:
            if c not in string.ascii_letters and c != " ":
                raise InvalidArgumentException("Name must contain only contain ASCII letters", name)
        

if __name__ == "__main__":
    try:
        p1 = Person("L337 Hansen")
    except InvalidArgumentException as e:
        print(e)
        
    try:
        p2 = Person("Lars Larsen")
    except InvalidArgumentException as e:
        print(e)

    try:
        p3 = Person("Leonardo di Caprio")
    except InvalidArgumentException as e:
        print(e)
