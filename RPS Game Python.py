import random
human = 0
computer = 0
name = input("What is your name?")
print("Hello",name)
def Game():
        global human
        global computer
        print("Computer score:", computer)
        print("Your score:", human)
        choice = input("Okay " + name  + " Please choose Rock, Paper, or Scissors ")
        choice = choice.lower()
        while (choice != "rock" and choice != "paper" and choice != "scissors"):
            print(choice);
            choice = input("That choice is not valid. Enter your choice (rock/paper/scissors): ");
            choice = choice.lower()
        compGuess = random.randint(0,2)
        if (compGuess == 0):
                comp = "rock";
        elif (compGuess == 1):
            comp = "paper";
        elif (compGuess == 2):
            comp = "scissors";
        else:
            comp = "Bad noises";

        if (choice == comp):
            print("Its a draw");
        elif (choice == "rock"):
                if (comp == "paper"):
                        print("Computer wins!")
                        computer += 1;
                else:
                        print("You win!")
                        human += 1;
        elif (choice == "paper"):
                if (comp == "rock"):
                        print("You win!")
                        human += 1;
                else:
                        print("Computer wins!")
                        computer += 1
        elif (choice == "scissors"):
                if (comp == "rock"):
                        print("Computer wins!")
                        computer += 1;
                else:
                        print("You win!")
                        human += 1;

while human < 5 and computer < 5:
    Game()
        
if  human == 5 or computer == 5:
    end = input("Do you want to play again Yes or No").lower()
    if (end == "yes"):
        human = 0
        computer = 0
        Game()
    else:
        pass
