import random
choose = int(input("1, 2"))
if choose == 1:
    a = random.randint(1, 5)
    choose = int(input("1, 2, 3, 4, 5"))
    print(choose);
if choose == 1:
  a = random.randint(1, 10)
  print("Clerk",a);
elif choose == 2: 
  a = random.randint(10, 50)
  print("Manager",a);
elif choose == 3: 
  a = random.randint(10, 50)
  print("Tester",a);
elif choose == 4: 
  a = random.randint(10, 50)
  print("Developer",a);
elif choose == 5: 
  a = random.randint(10, 50)
  print("Exit",a);

else:
  print("Invalid input")
  print(num);

if choose == 2:
    a = random.randint(1, 5)
    choose = int(input("1, 2, 3"))
    print(choose);

if choose == 1:
  a = random.randint(1, 10)
  print("name",a);
elif choose == 2: 
  a = random.randint(10, 50)
  print("age",a);

elif choose == 3: 
  a = random.randint(10, 50)
  print("Exit",a);

else:
  print("Invalid input")
  print(num)
  
