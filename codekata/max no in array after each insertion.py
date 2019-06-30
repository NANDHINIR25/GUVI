ip1,ip2=map(int,input().split())
d=input()
lis1=list(map(int,input().split()))
lis2=list(map(int,input().split()))
for i in lis2:
  lis1.append(i)
  print(max(lis1),end=" ")
