import random
choose = int(input("1, 2, 3, 4"))
if choose == 1:
  print("clerk");
  print("Manager");
  print("Tester");
  print("Developer");
  print("Exit");
  
if choose == 2:
  print("Clerk");
  name= input("enter name :");
  age= int(input("enter age :"));
  salary= int(input("enter salary :"));
  print("Manager");
  name= input("enter name :");
  age= int(input("enter age :"));
  salary= int(input("enter salary :"));
  print("Tester");
  name= input("enter name :");
  age= int(input("enter age :"));
  salary=int(input("enter salary :"));
  print("Developer");
  name= input("enter name :");
  age= int(input("enter age :"));
  salary= int(input("enter salary :"));
  a = random.randint(1, 10)
  print("exit");

elif choose == 3:
  a = random.randint(1, 10)
  choose = int(input("1, 2, 3, 4, 5"))
  print(choose);
  
if choose == 1:
  a = random.randint(1,10)
  print("Clerk",a);
  c=int(input("Enter salary :"));
  p=int(input("percent increased :"));
  p=p*(c/100);
  c=c+p;
  print("increased salary :",c);
elif choose == 2:
  a = random.randint(1, 10)
  print("Manager",a);
  c=int(input("Enter salary :"));
  p=int(input("percent increased :"));
  p=p*(c/100);
  c=c+p;
  print("increased salary :",c);
elif choose == 3:
  a = random.randint(1, 10)
  print("Tester",a);
  c=int(input("Enter salary :"));
  p=int(input("percent increased :"));
  p=p*(c/100);
  c=c+p;
  print("increased salary :",c);
elif choose == 4:
  a = random.randint(1, 10)
  print("Developer",a);
  c=int(input("Enter salary :"));
  p=int(input("percent increased :"));
  p=p*(c/100);
  c=c+p;
  print("increased salary :",c);
elif choose == 5: 
  a = random.randint(1)
  print("Exit",a);

elif choose == 4:
  print("exit");


  
