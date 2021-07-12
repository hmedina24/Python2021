def main():
    name = raw_input("What is your name? ")  
    age = input("What is your age? ")
    year = (100 - age) + 2021
    print("Your name is: " + name)
    print("You will turn 100 this year: " + str(year))

if __name__ == "__main__":
    main()