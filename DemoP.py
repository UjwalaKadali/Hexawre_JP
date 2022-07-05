class DemoP:
    name="Ram";
    def __init__(self,name,age,salary):
        print("constructor");
        self.name=name;
        self.age=age;
        self.salary=salary;

    def mthod(self):
        print("hii");
        print("name:",self.name);
        print("age:",self.age);
        print("salary:",self.salary);

class D (DemoP):
    def __init__(self):
        print("d class constructor",self.name);

d=DemoP("raj",25,35000);
d.mthod();

d1=D();
        
