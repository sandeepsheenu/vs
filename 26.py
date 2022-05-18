import re 
def regex(txt):

 regex="[0-9]{4}"
 p=re.compile(regex)

 if(re.search(p,txt) and
        len(txt) == 4):
       print("true")
 else:
    print(False)  


regex("8476")
