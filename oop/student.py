from datetime import datetime


class Student:
    students_count = 0
    
    def __init__(self, fname, lname, yob, grade, section):
        self.fname = fname
        self.lname = lname
        self.yob = yob
        self.grade = grade
        self.section = section

        Student.students_count += 1

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def classroom(self):
        return f"Grade {self.grade} {self.section}"

    def age(self):
        current_year = datetime.now().year
        return current_year - self.yob

    def __str__(self):
        return self.fullname()
