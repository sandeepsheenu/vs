import re
txt="pink flag red flag black flag blue flag green flag red flag"
n=["redflag","Blueflag"]
x=re.findall(n,txt)
print(x)