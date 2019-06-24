ip1=int(input())
sum=0
while(ip1>0):
  dig=ip1%10
  x=dig**2
  sum=sum+x
  ip1=ip1//10
print(sum)
