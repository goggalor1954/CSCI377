# James Roesemann
# Insertion sort
# Homework 1
# due 6/12/18

import random
random.seed()

insertionList=[]
numOfVar = input( 'How many variables do you want to test? ')

# generate random integers 'numOfVar' times. 
for x in range(0, numOfVar):
	insertionList.append(random.randint(0,100))

# print our unsortred list
print ('This is our unsorted list:')
for x in insertionList:
	print(x)

# perform insertion sort on list
for index in range(1, len(insertionList)):
#	print x
	key=insertionList[index]
	position=index-1

	while position>=0 and key <insertionList[position]:
		insertionList[position+1]=insertionList[position]
		position-=1
	insertionList[position+1]=key

print('this is our sorted list')
for x in insertionList:
	print(x)


