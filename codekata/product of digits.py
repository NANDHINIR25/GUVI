ip=int(input())
product=1
while(ip>0):
  dig=ip%10
  product=product*dig
  ip=ip//10
print(product)
