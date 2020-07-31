# sum of even numbers in 0 - 100
sum = 0
for x in range(100,0,-2):
    sum += x
print(sum)



### or

evensum = 0
for x in range(101):
    if x%2 == 0 :
        evensum += x
print(evensum)