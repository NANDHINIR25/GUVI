ip=int(input())
rev=0
while(ip>0):
  dig=ip%10
  rev=rev*10+dig
  ip=ip//10
print(rev)
