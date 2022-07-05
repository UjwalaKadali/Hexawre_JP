class Employee:
            def __init__(self):
        self.uid=input("enter ID:");
        self.name=input("enter Name:");
        self.age=input("enter age:");
        self.salary=input("enter salary:");
        self.designation=input("enter designation:");

    def display(self):
        print("Id:",self.uid)
         print("Name:",self.name);
          print("Age:",self.age)
         print("salary:",self.salary)
          print("Designation:",self.designation)

e=Employee();
e.display();
