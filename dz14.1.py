class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} лет, {self.gender}'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return super().__str__() + f', Зачетная книжка: {self.record_book}'

class GroupLimitError(Exception):
    def __init__(self, message="Превышен лимит группы: максимум 10 студентов"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)
    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Номер группы: {self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN143')
st4 = Student('Female', 23, 'Anna', 'Smith', 'AN146')
st5 = Student('Male', 21, 'Paul', 'Brown', 'AN147')
st6 = Student('Female', 24, 'Laura', 'White', 'AN148')
st7 = Student('Male', 20, 'Mark', 'Green', 'AN149')
st8 = Student('Female', 22, 'Emma', 'Black', 'AN150')
st9 = Student('Male', 23, 'David', 'Clark', 'AN151')
st10 = Student('Female', 21, 'Sophia', 'Lewis', 'AN152')
st11 = Student('Male', 22, 'James', 'Walker', 'AN153')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for student in students:
    try:
        gr.add_student(student)
        print(f"Студент {student.first_name} {student.last_name} добавлен в группу.")
    except GroupLimitError as e:
        print(e)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')

