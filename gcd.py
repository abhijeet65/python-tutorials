from random import randrange
from math import sqrt

def gcd1(n,m):
 min=n if n<m else m
 max=m if m<n else n
 
 for i in range(min,min+1):
  if n%i==0 and m%i==0 :
   print("found","->",i)
   i-=1
   

def gcd(m,n):
  
 if n==0:
  return m
 #elif n>m:
  #return gcd(n,m)
 else:
  return gcd(n,m%n)





d=gcd(13,56)
print(d)
