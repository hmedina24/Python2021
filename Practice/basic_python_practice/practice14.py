#Write a program (using functions!) that asks the user for a long string contains multiple words. 
#Print back to the user the same string, except with the words in backwards order.

def main():
    #get user input
    user_input = raw_input("Type a sentence > ")
    #convert string to elements and store inside the array
    conversion = user_input.split(" ")
    #reverse the array with the reverse function or with slicing  
    #conversion.reverse()
    #join the elements and return string 
    print(" ".join(conversion[::-1]))

if __name__ == "__main__":
    main()