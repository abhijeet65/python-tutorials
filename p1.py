from math import sqrt
a=[] 
def prime(n):
 
 for i in range(2,n+1):
  a.append(i)
 for p in range(2,int(sqrt(n))):
  if a[p]!=0:
   j=p*p
   while(j<=n):
    a.remove(j)
    a.insert(j,0)
    j=j+p

prime(20)
print(a)
