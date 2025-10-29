num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
    if sum==num:
       print("amstrong number")
    else:
        print("Not a armstrong number")
        
        
