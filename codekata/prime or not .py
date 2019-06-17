ip1=int(input())
if ip1>0:
  for i in range(2,ip1):
    if(ip1%i==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
