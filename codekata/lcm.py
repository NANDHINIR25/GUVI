n1,n2=map(int,input().split())
l= 1
while(l<=n1 and l<=n2):
  if(n1%l==0 and n2%l==0):
    hcf=l
    lcm=(n1*n2)/hcf
  l=l+1
print(int(lcm))       
