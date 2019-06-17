ip1=input()
dig=False
alpha=False
for i in ip1:
  if(i.isdigit()):
    dig=True
  if(i.isalpha()):
    alpha=True
if(dig and alpha):
    print("yes")
else:
    print("no")
    
