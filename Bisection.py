from math import *

fx = input("Enter the expression : ")

x=0
if("log" in fx):
    x=1

a=eval(fx)
x=x+1
b=eval(fx)
if (a<0 and b>0) or (a>0 and b<0):
    print("\nRoots lie between ({},{})".format(x-1,x))
else:
    while a!=0 and b!=0 :
        if (a<0 and b>0) or (a>0 and b<0):
            break
        x=x+1
        a=eval(fx)
        if (a<0 and b>0) or (a>0 and b<0):
            break
        x=x+1
        b=eval(fx)
    print("\nRoots lie between ({},{})".format(x-1,x))
    
p=x-1
float(p)
q=x
float(q)
m=1
n=2
i=0

while m!=n:
    i=i+1
    print("\n{} Approximation :- ".format(i))
    xa=(p+q)/2
    print("x{} = {}".format(i,xa))
    x=xa
    y=eval(fx)
    print("f({}) = {}".format(x,y))
    if y<0:
        p=xa
        print("Roots lies between ({},{})".format(p,q))
    if y>0:
        q=xa
        print("Roots lies between ({},{})".format(p,q))
    m=round(p,4)
    n=round(q,4)
    
print("\nTherefore, the root is {0:.4f}".format(m))    
