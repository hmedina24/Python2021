# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.).
# Take this opportunity to practice using functions.
def prime_or_not(num):
    if num > 0:
        for x in range ( 2, num - 1):
            if num % x != 0:
                continue
            elif num % x == 0:
                return "The number is not prime."
        return "The number is prime."
    elif num == 0:
        return "The number is not prime."
    else:
        return "The number is not prime."


def main():
    user_input = int(input("Enter a number: "))

    print(prime_or_not(user_input))
    

if __name__ == "__main__":
    main()