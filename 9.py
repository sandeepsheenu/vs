def nested(a,b):
    if min(a)>min(b)  and max(a)<max(b):
        print(True)
    else:
        print(False)    

nested([1, 2, 3, 4], [2, 3])    