# James Roesemann
# CSCI377
# Homework 1
# Insertion sort
# due 6/12/18




# perform an insertion sort of a given list 'insertList'
def insertSort(insertList):
	for index in range(1, len(insertList)):
		key=insertList[index]
		position=index-1

		while position>=0 and key <insertList[position]:
			insertList[position+1]=insertList[position]
			position-=1
		insertList[position+1]=key


	











