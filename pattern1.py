from random import randrange

n=randrange(1,10)
for i in range(1,n+1):
 for j in range(i,n+1):
  print(j,end="")
 print()

for i in range(1,n+1):
 for j in range(1,i+1):
  print(j,end="")
 print()

for i in range(1,n+1):
 for j in range(i,n+1):
  print(i,end="")
 print()
print(end="-----------------------------")
print()

for i in range(1,n+1):
 for j in range(1,i+1):
  print(" ",end="")
 for k in range(1,n-i+1):
  print(k,end="") 
 print()
 

a=[1,2,3,4,5]
b=[2,3,5,6]
p=a+b
print(sorted(p))
print(p)
p.sort()
p.append(0)
print(p)


