#Make a two-player Rock-Paper-Scissors game.
#(hint: ask for player plats (using input), compare them, print out a message of congratulations to the winner, and ask if the plays want to start a new game)
#Remeber the rules:
#	Rocks beats scissors
#	Scissors beats paper
#	Paper beats rock

def compare(choice_1, choice_2):
    if choice_1 == choice_2:
        return("It is a Tie!")
    elif choice_1 == "rock":
        if(choice_2) == "scissors":
            return("rock wins!")
        else:
                return("papers wins!")
    elif choice_1 == "scisssors":
        if(choice_2) == "paper":
            return("scissors wins!")
        else:
            return("rock wins!")
    elif choice_1 == "paper":
        if(choice_2) == "rock":
            return("paper wins!")
        else:
            return("scissors wins!")
    else:
        return("Invalid input!")

def main():
    print("----Beginning of the game----")
    user_input = raw_input("Want to play a game? Y/N: ")
    if user_input == 'N':
        print("Ok then, never mind!")
    else:
        while(user_input != 'N'):
            user_choice_1 = raw_input("Rock, paper, or scissors. Shoot! ")
            user_choice_2 = raw_input("Rock, paper, or scissors. Shoot! ")
            
            print(compare(user_choice_1,user_choice_2))

            user_input = raw_input("Would you like to play again? Y/N: ")
    print("----End of the Game----")

if __name__ == "__main__":
    main()