from random import randrange
def sort(a):
 n=len(a)
 for i in range(0,n-1):
  pos=i
  for j in range(i+1,n):
   if a[j]<=a[pos]:
    pos=j
  if pos!=i:
   a[pos],a[i]=a[i],a[pos]

def main():
 for i in range(0,5):
  print(randrange(1,10))

 a=[]

 count=randrange(3,15)

 for i in range(count):
  a+=[randrange(2,40)]

 print(a)
 print(count)

 results=list(range(0,32))
 print(results)
 sort(a)
 print(a)




main()
