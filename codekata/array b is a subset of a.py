ip1,ip2=input().split()
li=list(input())
li1=list(input())
count=0
for i in range(0,len(li1)):
  if(li1[i]==li[i]):
    count=1
if(count==1):
  print("yes")
else:
  print("no")
