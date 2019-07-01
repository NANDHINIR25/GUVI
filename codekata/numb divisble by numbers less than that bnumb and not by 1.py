ip1=int(input())
c=0
for i in range(2,ip1):
  if(ip1%i==0):
    c=1
if(c==1):
  print("yes")
else:
  print("no")
