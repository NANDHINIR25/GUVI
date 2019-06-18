A,B,C=map(int,input().split())
AP=0
for i in range(1,C+1):
 AP+=A+(C-i)*B
print(AP)
