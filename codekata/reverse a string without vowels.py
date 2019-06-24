num=int(input())
ip1=input()
ip2=['a','e','i','o','u']
for x in ip2:
  if x in ip1:
    ip1=ip1.replace(x,"")
print(ip1[::-1])

