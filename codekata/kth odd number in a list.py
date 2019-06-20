ip1,ip2=map(int,input().split())
lis1=list(map(int,input().split()))
lis2=[]
for i in range(0,len(lis1)):
   if((lis1[i])%2!=0):
     lis2.append(lis1[i])
print(lis2[ip2-1])
