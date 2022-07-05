a=int(input("enter Science value:"));
b=int(input("enter Social value:"));
c=int(input("enter english value:"));
d=int(input("enter telugu value:"));
e=int(input("enter Maths value:"));
f=a+b+c+d+e;
print("total is:",f);
h=f/6;
print("result :",h);
if h>90:
    Print("Good");
elif h<90 and h>45:
    print("Avg");
else:
    print("poor");
