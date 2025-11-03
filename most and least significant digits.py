# Program to find the most and least significant digits of a number

num = int(input("Enter a number: "))

# Get the least significant digit (last digit)
least = num % 10

# Get the most significant digit (first digit)
most = num
while most >= 10:
    most = most // 10

print("Most significant digit:", most)
print("Least significant digit:", least)
