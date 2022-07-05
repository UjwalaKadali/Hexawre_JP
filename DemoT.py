f= open("DemoZ.py","x");
a=open("DemoZ.py","a");
name=input("enter name:");
age=input("enter age");
salary=input("enter designation:");
a.write(name)
a.write(age)
a.write(salary)
a.write(designation);
a.close();
readdate=open("DemoZ","r");
print(readdate.read());
