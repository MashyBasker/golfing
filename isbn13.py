n=int(input())
odd=0
even=0
for i in range(len(str(n))):
    if i%2==0:
        even+=int(str(n)[i]) 
    else:
        odd+=int(str(n)[i])