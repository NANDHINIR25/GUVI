ip1=int(input())
for i in range(1,ip1+1):
  if((ip1%i==0) and (i%2==0)):
      print(i,end=' ')
