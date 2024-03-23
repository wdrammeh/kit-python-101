from datetime import datetime


class Student:
    students_count = 0
    
    def __init__(self, fname, lname, yob, grade, section):
        self.fname = fname
        self.lname = lname
        self.yob = yob
        self.grade = grade
        self.section = section
        Student.increment_count()

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def classroom(self):
        return f"Grade {self.grade} {self.section}"

    def age(self):
        current_year = datetime.now().year
        return current_year - self.yob

    def __str__(self):
        return self.fullname()

    @classmethod
    def increment_count(cls):
        cls.students_count = cls.students_count + 1
        
    @classmethod
    def get_count(cls):
        return cls.students_count
    
    @staticmethod
    def is_school_day():
        current_day = datetime.now().weekday()
        if current_day == 5 or current_day == 6:
            return False
        return True
    