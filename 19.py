from pickle import APPEND


def arrayOfMultiples(num,length):
    l1=[]
    for j in range(1,length+1):
        c=num*j
        l1.append(c)
    print(l1)    

arrayOfMultiples(7,5)
