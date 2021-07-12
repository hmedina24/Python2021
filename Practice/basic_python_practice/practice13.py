#write a program(function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Extras:
#	write two difference functions to do this one using a loop and construsting a list, and another one using sets.
#	go back and do Excersis 5 using sets, and write the solution for that in different function 

# a,1,1,2,3,5,8,13,21,34,55,89
def main():
    #store nums in array
    a = map(int, "1,1,2,3,5,8,13,21,34,55,89".split(","))
    #2 ways of creating sets of integers and with duplicates removed 
    c = set(b)
    d = {x-1 for x in a}
    #list comprenhension from set to list  
    b = [x for x in c]
    
    
if __name__ == "__main__":
    main()