#Create 2 random lists of numbers and output a list of overlapping numbers
#between the 2 lists.

import random

randomList1 = random.sample(range(1,100),10)
randomList2 = random.sample(range(1,100),10)

overlapList = []

for num1 in randomList1:
	for num2 in randomList2:
		if num1 == num2:
			overlapList.append(num1)

print(randomList1)
print(randomList2)
print(overlapList)