a = 2
b = 5
count = 0
res = 1
while(b>0):
    
    count+=1
    if(b & 1):
        res = res*a
    a= a*a
    b>>=1


print(res)