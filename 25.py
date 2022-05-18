l1=["1a", "a", "2b", "c"]
m=[]
for i in l1:
    for j in i:
        if (j.isdigit()):
            m.append(i)
          
print(m)