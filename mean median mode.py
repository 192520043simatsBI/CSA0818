import statistics
numbers=list(map(float,input("enter numbers seperated by space:").split()))
mean=statistics.mean(numbers)
median=statistics.median(numbers)
mode=statistics.mode(numbers)
print("mean:",mean)
print("median:",median)
print("mode:",mode)
