from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, yob):
        self.__name = name
        self.__yob = yob

    def get_yob(self):
        return self.__yob

    def get_name(self):
        return self.__name

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        info = super().describe()
        print(f'Student - {info}, Grade : {self.__grade} ')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        info = super().describe()
        print(f'Teacher - {info}, Subject : {self.__subject} ')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        info = super().describe()
        print(f'Doctor - {info}, Specialist : {self.__specialist} ')


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__people = []

    def add_person(self, person):
        self.__people.append(person)

    def describe(self):
        print(f'Name {self.__name} ')
        for person in self.__people:
            person.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__people:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_age(self):
        self.__people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        counter = 0
        total_year = 0
        for p in self.__people:
            if isinstance(p, Teacher):  # if type(p) is Teacher:
                counter += 1
                total_year += p.get_yob()
        return total_year/counter


student1 = Student('Hai', 1997, 7)
student1.describe()

teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()


teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()
ward1.sort_age()
ward1.describe()
