class Student:
    def __init__(self, student_name = 'Davit Grigoryan', marks='0'):
        self.student_name = student_name
        self.marks = marks
    def tell(self):
        return f'Student name: {self.student_name}\nStudent marks: {self.marks}'
student_orig = Student()
print(student_orig.tell())

student_second = Student('Mariam Ananyan', 6)
print(student_second.tell())
