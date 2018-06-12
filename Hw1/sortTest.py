# James Roesemann
# CSCI377
# Homework 1
# Sort Test
# due 6/12/18

#This a python script that will test the insertion sort and merge sort.
#The user will enter the initial number of variables to sort, and the range from which random variables will be generated.
#The user wil also enter either 'Insertion' or 'Merge'.
#An unsorted list will be generated and sorted.
#The results of the sort will be output to terminal.
#If the number of variables are less than 10, the sorted and unsorted versions of the list will also be output.
#This the number amd range of variables will be doubled, and sorts will reoccur, untill the sort time takes atleas 60 seconds.



# build a list of random ints of size 'num', of integers up to size 'size'
def buildList(sortList, num, size):
	for index in range (0, num):
		sortList.append(random.randint(0,size))

# print all the values of a list		
def printList(sortList):
	for index in sortList:
		print(index)

#calculates the time to sort and returns
def sortTime(timeStart):
	return time.time()-timeStart 

#if testMode is true, print the sort statment and the ordered values of the given list.
def testMode( sortCondition, sortList):
	print('\nThis is a %s list containing %d variables:' %(sortCondition, len(sortList)))
	printList(sortList)

#Prints the sort results. Takes the number of variables, the size of the range, the sort type and the sort start time.
def sortResults(numOfVar, size, sortType, timeElapsed):
	print('With %d variables ranging from 0 to %d, %s sort took %d seconds.'%(numOfVar, size, sortType,timeElapsed))

#performs either insert sort or merge sort depending on the passed 'sortType'.Calls test mode only the first time. then recursibly calls itself untill sort time exceds 60 seconds. starting testmode at 10 or less keeps the test size small and eliminates the need to write another recursive function
def repeatSort(numOfVar, size, sortType):
	sortList=[]
	buildList(sortList, numOfVar, size)
	if numOfVar<=10:
		testMode( 'unsorted', sortList)
	timeStart=time.time()
	#insertion dort
	if sortType == "Insertion":
		insertionSort.insertSort(sortList)
	#Merge sort
	if sortType == "Merge":
		sortList=mergeSort.mergeSort(sortList)
	if numOfVar<=10:
		testMode( sortType, sortList)
	timeElapsed=sortTime(timeStart)
	sortResults(numOfVar,size, sortType, timeElapsed)
	if timeElapsed<60:
		del sortList
		del timeStart
		del timeElapsed
		repeatSort(numOfVar*2, size*2, sortType)

	
import random
import time
import insertionSort
import mergeSort	


random.seed()
# initial number of variables
numOfVar = input('Enter How many variables to sort: ')
# initial range of variables
size=input('Enter range of vartiablees from 0 to : ')
sortType=raw_input('Enter "Insertion" for insertion Sort and "Merge" for Merge Sort: ')
if sortType!="Insertion" and sortType!="Merge":
	quit(0)
repeatSort(numOfVar, size, sortType)
