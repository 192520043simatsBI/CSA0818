pos_sum = 0
neg_sum = 0
pos_count = 0
neg_count = 0

num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    if num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

    num = int(input("Enter a number (-1 to stop): "))

# Find averages
if pos_count > 0:
    pos_avg = pos_sum / pos_count
else:
    pos_avg = 0

if neg_count > 0:
    neg_avg = neg_sum / neg_count
else:
    neg_avg = 0

print("Average of positive numbers:", pos_avg)
print("Average of negative numbers:", neg_avg)
