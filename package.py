from mypackage import mod1
from mypackage import mod2
from mypackage import mod3

m=int(input("enter the first number:"))
n=int(input("enter the second number:"))
a=mod1.sum(m,n)
print("sum",a)
b=mod2.avg(m,n)
print("avg",b)
p1=mod3.power(m)
print("power of",m,"is",p1)
p2=mod3.power(n)
print("power of",n,"is",p2)
