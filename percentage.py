class Student:
    def __init__(self):
        self.marks = []
        self.total_subjects = 0

    def input_marks(self):
        self.total_subjects = int(input("Enter the total number of subjects: "))
        for i in range(self.total_subjects):
            mark = float(input(f"Enter the marks for subject {i + 1}: "))
            self.marks.append(mark)

    def calculate_percentage(self):
        if self.total_subjects == 0:
            return 0
        total_marks = sum(self.marks)
        percentage = (total_marks / (self.total_subjects * 100)) * 100
        return percentage

    def display_percentage(self):
        percentage = self.calculate_percentage()
        print(f"Your percentage is: {percentage:.2f}%")

# Example usage:
student = Student()
student.input_marks()
student.display_percentage()
student.calculate_percentage()