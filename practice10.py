#Randomly generate 2 lists and produce another list with the overlapping numbers
#using list comprehension

import random

a = random.sample(range(1,100),10)
b = random.sample(range(1,100),10)

overlap = [num1 for num1 in a for num2 in b if num1 == num2]

print(a)
print(b)

print(overlap)