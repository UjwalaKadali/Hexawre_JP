f = open("DemoA4.py","x");
a = open("DemoA4","a");
a.write("/n clerk");
a.write("/n Manager");
a.write("/n tester");
a.write("/n Developer");
a.write("/n Exit");
n2=int(input("choose the option:"));
if(n==2):
    n2=int(input("choose the option:"));
if(n2==1):
    print("clerk details")
    c.display();
if(n2==2):
    print("Manager details")
    c.display();
if(n2==3):
    print("Tester details")
    c.display();
if(n2==4):
    print("Devloper details")
    c.display();
    
    
class clerk:
    def __init__(self):
        self.uid=int(input("enter id"));
        self.name=int(input("enter name"));
        self.age=int(input("enter age"));
        self.designation=int(input("enter designation"));
class Manager:
    def __init__(self):
        self.uid=int(input("enter id"));
        self.name=int(input("enter name"));
        self.age=int(input("enter age"));
        self.designation=int(input("enter designation"));
class Tester:
    def __init__(self):
        self.uid=int(input("enter id"));
        self.name=int(input("enter name"));
        self.age=int(input("enter age"));
        self.designation=int(input("enter designation"));
class Devloper:
    def __init__(self):
        self.uid=int(input("enter id"));
        self.name=int(input("enter name"));
        self.age=int(input("enter age"));
        self.designation=int(input("enter designation"));
        

        
        
a.close();
