"""
A Ward consists of a name (string) and a list of people in the Ward. 
A person can be a student, doctor, or teacher. 
A student has a name, year of birth (yob) (int), and grade (string). 
A teacher has a name, yob, and subject (string). 
A doctor has a name, yob, and specialist (string). 
Note that a list should be used to contain the list of people in the Ward.
"""

class Person:
    def __init__(self,name,yob):
        self.name = name
        self.yob = yob

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")

class Ward:
    def __init__(self,name_ward):
        self.name_ward = name_ward
        self.lst_people = []

    def add_person(self, person):
        self.lst_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name_ward}")
        for person in self.lst_people:
            person.describe()

    # Count doctor 
    def count_doctor(self):
        result = 0
        for person in self.lst_people:
            if isinstance(person,Doctor):
                result += 1
        return result

    # sort age 
    def sort_age(self):
        self.lst_people.sort(key = lambda person: person.yob)
    
    # compute average
    def compute_average(self):
        lst_age_teacher = [person.yob for person in self.lst_people if isinstance(person,Teacher)]
        return sum(lst_age_teacher) / len(lst_age_teacher)
    
# Test case
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name_ward="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")