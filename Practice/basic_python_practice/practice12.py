#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this oppurtunity to think about how you can use functions. Make sure to ask the user to enter the numbers of numbers in the sequence
#to generate.
#hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum of the previus two numbers in the sequence.
#sequence looks like this: 1,1,2,3,5,8
def fibonnaci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def main():
    user_input = int(input("Enter a number for the fibonnaci sequence: "))
    print(fibonnaci(user_inpute))

if __name__ == "__main__":
    main()