class Number():
    def __init__(self) -> None:
        self.num = 0
    def incr(self):
        self.num += 1
    def decs(self):
        self.num -= 1

class newNo(Number):
    def __init__(self) -> None:
        super().__init__()
    def sho(self):
        print(f"Value: {self.num}")

newNumber = newNo()
newNumber.incr()
newNumber.incr()
newNumber.decs()
newNumber.incr()
newNumber.incr()
newNumber.sho()


# object class

#Multi level inheritance

# class Coder():
#     def code(self):
#         print('Coding')
# class pythoner(Coder):
#     def py_code(self):
#         print("Coding web")
# class Django(pythoner):
#     def web_dev(self):
#         print("New.html @ django")

# web = Django()
# web.code()
# web.py_code()
# web.web_dev()

# #Multiple Inheritance
# class Coder():
#     def __init__(self):
#         self.name = input("Name >")
# class pythonner():
#     def __init__(self):
#         self.works = input("Works")
    
# class webDev(Coder, pythonner):
#     def __init__(self):
#         Coder.__init__(self)
#         pythonner.__init__(self)
#     def start_new(self):
#         print("New web jonb @django")

# webn = webDev()
# webn.start_new()

# Start off by creating the Result class
class Result:
    def __init__(self, students):
        self.dict = students
    # def show(self):
    #     # Print the entire dictionary
    #     print(self.dict)
    def add_rslt(self, student, marks):
        # Add or update the student's marks in the dictionary
        self.dict[student] = marks

class Student(Result):
    def __init__(self, students):
        super().__init__(students)
    
    def sho_rslt(self, student):
        # Print the student's result in the specified format
        if student in self.dict:
            print(f"{student} got {self.dict[student]}")
        else:
            print(f"{student} is not found in the records")

# Example usage
students = {
    "A": 88,
    "B": 71,
    "C": 84,
    "D": 95,
    "E": 60,
    "F": 89,
}

std = Student(students)  # Use Student class to inherit from Result

# Add new results
std.add_rslt("G", 85)
std.add_rslt("H", 67)

# Show all results
# std.show()  # Output: {'A': 88, 'B': 71, 'C': 84, 'D': 95, 'E': 60, 'F': 89, 'G': 85, 'H': 67}

# Show individual results
std.sho_rslt("A")
std.sho_rslt("B")  # Output: A got 88
# std.sho_rslt("G")
std.sho_rslt("D")  # Output: G got 85
std.sho_rslt("F")  # Output: H got 67
std.sho_rslt("H")  # Output: Z is not found in the records
