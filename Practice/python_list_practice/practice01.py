#Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
def main():
	list1 = [54, 44, 27, 79, 91, 41]
	#removes or deletes the item by index
	del list1[4]
	#add to a specific index of the list 
	list1.insert(2, 30)
	#add to the end of the list 
	list1.append(100)
	#result list1 = [54, 44, 30, 27, 79, 41, 100]
	print(list1)

if __name__ == "__main__":
	main()
