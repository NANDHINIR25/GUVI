n1=int(input())
c=0
for i in range(2,n1):
  if(n1%i==0):
     c=c+1
if(c!=2):
  print("yes")
else:
  print("no")  
