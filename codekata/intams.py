n,m=(input().split())
n=int(n)
m=int(m)
for x in range(n,m):
  ams=0
  temp=x
  while(temp>0):
    dg=temp%10
    ams+=dg**3
    temp//=10
    if(x==ams):
      print(x,end=' ')
  
