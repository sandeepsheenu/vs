def depth(a): 
   m=(str(a))
   c=0
   for j in m:
      if "["==j:
        c+=1
   print(c)