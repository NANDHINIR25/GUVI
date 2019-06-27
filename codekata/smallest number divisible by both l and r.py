ip1,ip2=map(int,input().split())
for i in range(1,10001):
  if((i%ip1==0) and (i%ip2==0)):
    print(i)
    break
