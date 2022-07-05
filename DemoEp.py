f = open("DemoEmp5.py","x");
a = open("DemoEmp5","a");
class Employee:
    def create(self):
        print("1.create")
        print("2.Display")
        print("3.exit")
class Display:
    def display(self):
        print("1.Clerk")
        print("2.Developer")
        print("3.Manager")
        print("4.Exit")
class Display1:
    def __init__(self):
        self.id=(input("enter id:"))
        self.name=(input("enter name:"))
        self.age=(input("enter age:"))
        self.salary=(input("enter salary:"))

    def display(self):
        print("id:",self.id)
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)

class Demo:
    d=Display();
    e=Employee();
    e.create();

    ch=int(input("enter your option"))
    if ch==1:
        d.display();
        ch1=int(input("enter the option:"))
        d1=Display1();
        e.create();
        ch2=int(input("enter the option:"))
        if ch2==2:
            d1.display();

    if ch==2:
        d.display();
        ch1=int(input("enter the option"))
        if ch1==1:
            d1=Display1();
            d1.display();
            e.create();
            ch3=int(input("enter the option"))
            d.display();
        if ch1==2:
            d1=Display1();
            d1.display();
            e.create();
        if ch1==3:
            d1=Display1();
            d1.display();
            e.create();
        if ch1==4:
            d1=Display1();
            d1.display();
            e.create();
        if ch1==5:
             exit(0);

    if ch==3:
         exit(0);
            

            
