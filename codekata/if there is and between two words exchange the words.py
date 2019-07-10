ip1=list(input().split())
if(len(ip1)>1):
  for i in range(len(ip1)):
    if(ip1[i]=='and'):
      ip1[i+1],ip1[i-1]=ip1[i-1],ip1[i+1]
  print(*ip1)
else:
  print(*ip1)
