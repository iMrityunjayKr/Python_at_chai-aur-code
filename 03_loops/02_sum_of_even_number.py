#Sum of even numbers
#problem: calculate the sum of even numbers up to a given number n.
n =10 # 2,4,6,8,9,10
sum_even = 0
for i in range(1, n+1):
    if(i%2==0):
        sum_even+=1
print("sum of even number is:",sum_even)
