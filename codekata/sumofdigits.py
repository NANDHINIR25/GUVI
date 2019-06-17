n=int(input())
sum=0
while(n>0):
  dig=n%10
  n=n//10
  sum=sum+dig
print(sum)
