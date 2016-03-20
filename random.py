import random
lit=[]
list=["kewal","saurabh","ajji","puke"]

for i in range(6):
  value=random.randint(0,3)
  print(value)
  
 # print("kewal" in list) TO CHECK IF ENTRY IS PRESENT IN THE LIST
  if(list[value] not in lit):
      print(list[value])
      lit.insert(i,list[value])

print(list)
print(lit)
