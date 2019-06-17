ip1,ip2=map(int,input().split())
ip1=ip1^ip2
ip2=ip1^ip2
ip1=ip1^ip2
print(ip1,ip2)
