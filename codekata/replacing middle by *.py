ip=list(input())
if len(ip)%2==0:
    ip[int(len(ip)/2)] ='*'
    ip[int(len(ip)/2)-1]='*'
else:
    ip[int(len(ip)/2)] ='*'
for i in range(0,len(ip)):
print(ip[i],end='')
