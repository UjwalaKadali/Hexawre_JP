try :
     age=int(input("enter age"))
    if age<18:
     raise ValueError;
    else:
     print('the age is value");
except ValueError as v:
     print("the age must be mroe than 18")
