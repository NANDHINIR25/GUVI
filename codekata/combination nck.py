import math
ip1,ip2=map(int,input().split())
x=int((math.factorial(ip1))/((math.factorial(ip2))*(math.factorial(ip1-ip2))))
print(x)
