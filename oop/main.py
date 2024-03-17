from student import Student

if __name__ == "__main__":
    maha = Student("Muhammed", "Drammeh", 1999, "10", "Art")
    eb = Student("Ebrima", "Sanneh", 2010, "9", "A")
    sul = Student("Sulayman", "Manjang", 2015, "7", "Pink")
    
    fullname = maha.fullname()
    fullname = Student.fullname(maha)
    print(fullname)
    # print(maha.classroom())
    # print(eb.fullname())
    # print(sul.fullname())
    
    print(Student.students_count)