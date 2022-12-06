import math

input_val = int(input())
result = math.exp(input_val) / (math.exp(input_val) + 1)
print(round(result, 2))
