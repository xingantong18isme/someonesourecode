import random
j1=0
j2=0
s=0
print("这是一个加法游戏")
while True:
  ji,j2=random.randint(0,1000),random.randint(0,1000)
  k=input("f"{j1}+{j2}=?")
  try:
    k=int(k)
  except:
    if k=="exit":
      break
    else:
      print("invaild value")
    
  else:
    if k==ji+j2:
      print("great!")
      s+=1
    else:
      print("not!")
  
