ip1,ip2,ip3 =list(map(str,input().split()))
ip3=int(ip3)
count=0
for a in range (len(ip1)):
  if ip1[a]!=ip2[a]:
     count+=1
if(count==ip3):
     print("yes")
else:
  print("no")
