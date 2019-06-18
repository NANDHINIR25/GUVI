n1,n2=map(int,input().split())
mul=n1*n2
for i in range(0,mul+1):
 if(i**2==mul):
  print('yes')
  break
else:
  print('no')
