
ip1=input()
ip2=""
for i in ip1:
  if i not in ip2:
    ip2=ip2+i
if(ip1==ip2):
  print("Yes")
else:
  print("No")
