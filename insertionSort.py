# James Roesemann
# Insertion sort
# Homework 1
# due 6/12/18

#This is a test of the insertion sort. 
#Variables will be input for the number and range of the variables to be sorted. 
#A bool variable will also be passed indicating wether the user wants to enable testing mode. 
#Testing mode will display the sorted and unsorted Variables 

# build a list of random ints of size 'num', of integers up to size 'size'
def buildList(insertList, num, size):
	for index in range (0, num):
		insertList.append(random.randint(0,size))

# print all the values of a list		
def printList(insertList):
	for index in insertList:
		print(index)

# perform an insertion sort of a given list 'insertList'
def insertSort(insertList):
	for index in range(1, len(insertList)):
		key=insertList[index]
		position=index-1

		while position>=0 and key <insertList[position]:
			insertList[position+1]=insertList[position]
			position-=1
		insertList[position+1]=key
"""
# if an inapropriate number is entered, warn the user and terminate the program.
def testValid(value):
	if value<=0 or type(value)!=int:
		print('Entry Invalid. Run the program again with a value > 0')
		exit(0)
"""


import random
import time

random.seed()
insertionList=[]
# input number of variables and range of variables. remove the test once the bash scipt is ready.
numOfVar = input()
testValid(numOfVar)
size=input()
testValid(size)

#build the unsorted list
buildList(insertionList, numOfVar, size)
#print the unsorted list. only uncomment during test
#print ('This is our unsorted list:')
#printList(insertionList)

#begin sort
timeStart=time.time()
insertSort(insertionList)
#print sorted list. only uncomment during test 
#print('This is our sorted list:')
#printList(insertionList)

#print time to sort
print('Sort took %d seconds.'%(time.time()-timeStart))




# write a bash script that can be used to input values to both programs
