def sevenboom(list_num):
 m=[]
 m=([int(d) for d in ''.join(str(x) for x in (list_num))])

 print(m)

 if 7 in m:
     print("boom")
 else:
     print("there is no 7 in the arr")


sevenboom([1, 2, 3, 4, 5, 6, 768,67,9])




