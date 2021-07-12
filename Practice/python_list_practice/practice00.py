#Given two lists create a third list by picking an odd-index element
#from the first list and even index elements from the second.
def main():
	#given list
	 listOne = [3,6,9,12,15,18,21]
	 listTwo = [4,8,12,16,20,24,28]
	 #list comprehension for even-index list and odd-index list
	 listThree = [listOne[x] for x in range(0, len(listOne)) if x % 2 !=0]
	 listFour = [listTwo[i] for i in range(0, len(listTwo)) if i % 2 == 0]
	 #results
	 print(listThree)
	 print(listFour)
	 print(listFour+listThree)
	 



if __name__ == "__main__":
	main()
