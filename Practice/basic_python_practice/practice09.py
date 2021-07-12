#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
#	Extra:
#		-keep the game going until the user types "exit"
#		-keep track of how many guesses the user has taken, and when the game ends print this out 
import random
def main():
    print("----Beginning of the Guessing Game---")
    user_guess = 0
    user_ans = raw_input("Do you want to play the guessing game? Y/N: ")
    if user_ans == "Y":  
        random_num = random.randint(1,9)
        while user_ans != "N":
            user_input = int(input("Pick a random number between 1 and 9: "))
            
            if user_input < random_num:
                print("Your guess was too low")
                user_guess += 1
            elif user_input > random_num:
                print("Your guess was too high")
                user_guess += 1
            elif user_input == random_num:
                print("After %d you guess the correct number. Congrat!" % user_guess)
            user_ans = raw_input("Do you want to take another guess? Y/N: ")
    else:
        print("Never mind then! ")
    print("----The game has ended----")
if __name__ == "__main__":
    main()