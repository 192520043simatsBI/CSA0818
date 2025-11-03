str=input("Enter a string:")
vcount=0
ccount=0
vowels="aeiouAEIOU"
c=[]
v=[]
for i in range(0,len(str)):
    if str[i] in (vowels):
        vcount=vcount+1
        v.append(str[i])
    elif(str[i]!=" " and str[i]not in(vowels)):
        ccount=ccount+1
        c.append(str[i])
print("the total number of vowel and constant are")
print(vcount,v)
print(ccount,c)
