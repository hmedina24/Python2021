#Take two lists, say for example these two:
#	a,1,1,2,3,5,8,13,21,34,55,89
#	b,1,2,3,4,5,6,7,8,9,10,11,12,13
#And write a program that returns a list that contains only the elements that are common between the list(without duplicates). 
#Make sure your program work two list of different sizes. 
#Extra:
#	1. Randomly generate two lists to test this
#	2. Write this in one line pof Python (don't worry if you can't figure this out at this point - we'll get to it soon)
def main():
    #creates a list of integers after splitting with the demlimiter = ,(comma)
    a = map(int, "1,1,2,3,5,8,13,21,34,55,89".split(","))
    b = map(int, "1,2,3,4,5,6,7,8,9,10,11,12,13".split(","))
    #concatenates both list to make a super list
    c = a + b
    #creates a empty array 
    ans = []
    #list comprenhension that seperates duplicates from the non-duplicate list 
    d = [ans.append(i) for i in c if i not in ans]
    
    print(ans)



if __name__ == "__main__":
    main()