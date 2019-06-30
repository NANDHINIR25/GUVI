ip1,ip2 = map(int,input().split())
count = 0
for i in range(1,10001):
  if i*i >= ip1 and i*i <= ip2:
       count += 1
print(count)
