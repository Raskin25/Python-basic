class student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def stu_details(self):
        print(f"your name is: {self.name}, your age is: {self.age} and your address is: {self.address}")
obj1=student("raskin",24,"Banasthali")
obj2=student("bikram",24,"chabahil")
# obj1.stu_details()
# obj2.stu_details()
print(obj1.stu_details(),obj2.stu_details())







