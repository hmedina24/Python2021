#Create a program that asks the user for a number and then prints out a list of all the divisors that number.
#(If you don't know what a divisor is, it is a number that divides evely into another number.) For example, 13 is a divisor of 26 /13 has no remainder.)
def main():
    num = int(input("Enter a number"))

    divisor = [i for i in range(1,num+1) if num % i == 0]

    print(divisor)

if __name__ == "__main__":
    main()