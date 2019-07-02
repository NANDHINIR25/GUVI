ip1,ip2,ip3=map(int,input().split())
if(((ip1+ip2)>=ip3) and ((ip2+ip3)>=ip1) and ((ip1+ip3)>=ip2)):
  print("yes")
else:
  print("no")
