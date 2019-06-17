word1=input()
i=0
for a in range (len(word1)):
 if(word1[a].isdigit() or word1[a].isalpha() or word1[a]==' '):
  continue
 else:
  i+=1
print(i)  
