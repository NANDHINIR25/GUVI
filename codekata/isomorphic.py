str1, str2 = input().split()
co = 0
for i in range(len(str1)):
  if str1.count(str1[i]) == str2.count(str2[i]):
    co += 1
if co == len(str1):
  print ("yes")
else:
  print ("no")
