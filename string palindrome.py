string=input("enter a string")
string=string.lower()
reverse_string=string[::-1]
if string==reverse_string:
    print("the given string is a palindrome")
else:
    print("the given string is not a palindrome")
