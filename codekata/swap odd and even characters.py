str=input()
for x in range(0,len(str)):
  if (x%2==0):
    print(str[x+1],end='')
  else:
    print(str[x-1],end='')
