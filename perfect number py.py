n=int(input("enter the to find if it is a perfect number"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("%d is a perfect number"%n)
else:
    print("%d is not a perfectnumber"%n)

