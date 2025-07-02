import random

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])


def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(user_choice == 'rock' and computer_choice == 'sciccors')or\
                     (user_choice == 'scissors' and computer_choice == 'paper')or\
                     (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


    def play_game():
        user_score=0
        computer_score=0

        while True:
            print("Welcome to Rock-Paper-Scissors!")
            print("Please choose:rock,paper,or scissors")
            user_choice = input("Your choice:").lower()

            if user_choice not in['rock','paper','scissors']:
                print("Invalid choice.Please choice again.")

                continue

            computer_choice=get_computer_choice()
            print(f"Computer choice:{computer_choice}")

            result = determine_winner(user_choice,computer_choice)
            print(result)


            if result == "You win!":
                user_score +=1
            elif result == "You lose!":
                computer_score +=1



                print(f"Score:You {user_score}-Computer{computer_score}")


                play_again = input("Do you want to play again?(yes/no):").lower()
                if play_again!='yes':
                    break


                print("Thanks for playing!")
                
                play_game()  
