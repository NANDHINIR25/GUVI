p1=int(input())
ip2=list(map(int,input().split()))
srt=ip2[:]
srt.sort()
for i in range(0,len(ip2)):
  if(ip2[i]!=srt[i]):
     print(i)
     break
