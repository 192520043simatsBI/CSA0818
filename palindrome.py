num=int(input("enter a number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("the given number is a palindrome.")
else:
    print("the given number is not a palindrome.")
    
