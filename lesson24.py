class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
    def display_info(self):
        average_grade = self.calculate_average()
        print (f"Student name: {self.name}, Student 10: {self.student_id}, Averages: {average_grade}")

student1 = Student("Alice Johnson", 101 )
student2 = Student("Bob Smith", 102)

student1.add_grade (85.0) 
student2.add_grade (78.5)

student1.display_info() 
student2.display_info()