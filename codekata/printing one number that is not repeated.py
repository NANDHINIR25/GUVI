ip1=int(input())
ip2=list(map(int,input().split()))
count=0
for i in range(0,ip1+1):
  if(ip2.count(i)==1):
   print(i)
   break
