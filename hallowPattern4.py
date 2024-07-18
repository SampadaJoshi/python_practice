n=int(input("enter num:"))
if n%2==0:
    n+=1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if j==1 or j==5 or i==j or (i+j)==(n+1):
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()