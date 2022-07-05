class Demo:
    def __init__(self):
        print("constructor");
        def display(self):
            print("hello");

class clerk:
     def __init__(self):
        print("clerk constructor");
        def salary(self):
            print("hello clerk");

class Dev(clerk,Demo):
     def __init__(self):
        print("Dev constructor");
        def raiseSalary(self):
            print("hello Dev");

d=Dev();
d.raiseSalary();
d.salary();
d.display();
