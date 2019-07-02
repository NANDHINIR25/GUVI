ip1,ip2=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l3.sort()
for i in range(len(l3)):
  print(l3[i],end=' ')
