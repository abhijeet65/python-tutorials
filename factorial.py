from math import *

def fact(n):
 res=1
 for i in range(1,n+1):
  res=res*i;
 return res

def prime(n):
  for i in range(2,int(sqrt(n))):
   if n%i==0:
    return "false"
  return "true"

def swap(x,y):
 x,y=y,x
 print(x,y,"swapped numbers",sep=":",end="")
 print("swapped numbers is {2} and {1} is {0} ".format(x,y,"cat"))

print(fact(5))
print(prime(20))
swap(10,20)
