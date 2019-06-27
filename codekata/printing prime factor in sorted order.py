ip1=int(input())
ip2=list()
for i in range(2,ip1+1):
  if((ip1%i)==0):
    ip2.append(i)
print(ip2,end=' ')
