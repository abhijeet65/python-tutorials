p=1
d={}
while(p):
 key=int(input("Enter the key"))
 value=int(input("Enter the value"))

 print(d)

 d.update({key:value})
 print(d)
 key=int(input("Enter the key"))
 value=int(input("Enter the value"))
 d.update({key:value})
 print(d)
 p=eval(input("Enter the chioce"))
 
 print(d.keys())
 print(d.values())
