ip1=input()
count=0
for i in range(len(ip1)):
  if((int(ip1[i])%2)==1):
    count=count+int(ip1[i])
if(count%2==0):
  print("E")
else:
  print("O")
