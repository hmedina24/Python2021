#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Extra: 
#       1. If the number is a multiple of 4, print out a different message. 
#       2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). Ifcheck divides evenly into num, tell that to the user. If not, print a different appropiate meesage. 

def main():
    num = int(input("Give me a number: "))
    check = int(input("Give me a number to divide by: "))
    
    if(num % 4 == 0):
        print("The number is a multiple of 4 and the number is even")
    elif (num % (2) == 0):
        print("the number is even")
    else:
        print("the number is odd")

    if num % check == 0:
        print(num, "divides evenly by, ", check)
    else:
        print(num, "does not divide evenly by, ", check)


if __name__ == "__main__":
    main()