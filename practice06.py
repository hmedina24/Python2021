#Ask the user for a string and print out wheter this string is panlindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)
def main():
    user_input = raw_input("Enter a sentence: ")
    str_lis = user_input.split(" ")
    str_lis.reverse()
    print(" ".join(str_lis))
    

if __name__ == "__main__":
    main()
