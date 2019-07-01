ip1=[]
ip2=int(input())
ip3=input().split()
for x in ip3:
  ip1.append(x)
ip1.sort()
ip1.sort(key=len)
for x in ip1:
  print (x,end=' ')
