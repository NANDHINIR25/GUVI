ip1=input().split()
ip2=input().split()
ip3=input().split()
if(ip1[0]==ip2[0]==ip3[0] or ip1[1]==ip2[1]==ip3[1] or (ip1[0]==ip1[1] and ip2[0]==ip2[1] and ip3[0]==ip3[1])):
    print('yes')
else:
    print('no')
