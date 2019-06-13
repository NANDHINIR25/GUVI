nu,mu=input().split()
nu=int(nu)
mu=int(mu)
for i in range(nu+1,mu):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break

    else:
      print(i,end=' ')
  else:
    break
