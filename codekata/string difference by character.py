ip1,ip2=input().split()
count=0
for i in range(0,len(ip2)):
  if(ip2[i]!=ip1[i]):
    count=count+1
if(count==1):
  print('yes')
else:
  print('no')
