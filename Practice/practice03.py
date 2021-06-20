#Take a list, say for example this one:  a = 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, 89 and write a program that prints out all the elements of the list that are less than 5. 
#Extra:
#	Instead of print the elements one by one, make a new list that has all elements less than 5 from this list in it and print out this new list.
#	Write this in one line of python.
#	Ask the user for a number and return a list that contains only elements from the original list a that smaller than that number given by the user 
def main():
    a = [1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, 89]
    #list comprehension for list b
    b = [i for i in a if i <= 5 ]
    #list comprenhension for list c
    num = int(input("Enter a number: "))
    c = [i for i in a if i <= num]
    
    print("List a: ", a)
    print("List b: ", b)
    print("List c: ", c)

if __name__ == "__main__":
    main()