# put your python code here
number_a = int(input())
number_b = int(input())

summed = 0
found = 0

for i in range(number_a, number_b + 1):
    if i % 3 == 0:
        found += 1
        summed += i

print(summed / found)
