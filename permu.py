from math import sqrt

def permut(prefix,suffix):
  
 if(len(suffix)==0):
  print(prefix) 
 else:
  for i in range(len(suffix)):
   new_pre=prefix+[suffix[i]]
   new_suffix=suffix[:i]+suffix[i+1:]
   permut(new_pre,new_suffix)
   

permut([],[1,2,3,4])
