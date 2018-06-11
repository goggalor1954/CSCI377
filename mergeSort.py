# James Roesemann
# CSCI377
# Homework 1
# Merge sort
# due 6/12/18

#this function sorts a list of integers.
#a list of integers is passed to the function.
#the ilst is split into two, recursivly, untill the list of size one.
#lists are then recursivly merged, untill it has been fully merged into one list.
#merge listA and listB, return sortedList
def mergeList(listA, listB):
	indexA=0
	indexB=0
	sortedList=[]
	#compares the lowest index element of list A and B. the lowest value gets added to Sorted List 
	while indexA<len(listA) and indexB<len(listB):
		if listA[indexA]<listB[indexB]:
			sortedList.append(listA[indexA])
			indexA+=1
		else:
			sortedList.append(listB[indexB])
			indexB+=1
	#copy any remaining elements of list a or b, if any remain. this is for the case when one list is bigger than the other.
	while indexA<len(listA):
		sortedList.append(listA[indexA])
		indexA+=1
	while indexB<len(listB):
		sortedList.append(listB[indexB])
		indexB+=1
	return sortedList

#if unsorted list is of size one, return. if not, split list into two lists. pass those lists to another merge sort, and merve the returned values
def mergeSort(unsortedList):
	if len(unsortedList)<=1:
		return unsortedList
	else:
		halfWay=len(unsortedList)/2
		listA=unsortedList[0:halfWay]
		listB=unsortedList[halfWay:len(unsortedList)]
		return mergeList(mergeSort(listA), mergeSort(listB))


