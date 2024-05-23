import random
def start_game():
    print("ROCK-PAPER-SCISSORS!")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    user=int(input("Select any options:"))
    print('Option choosed by user is:',end=' ')  #Display user's choice
    if user==1:
        print('Rock')
    elif user==2:
        print('Paper')
    else:
        print('Scissor')
    computer=random.randint(1,3)  #computer generates random choice
    print('Option choosed by machine is:',end=' ')   #Display computer's choice
    if computer==1:
        print('Rock')
    elif computer==2:
        print('Paper')
    else:
        print('Scissor')

    if user==computer:              #display's result
        print("Wow It's a tie!")
    elif user==1 and computer==3:
        print("Congratulations!!You won!")
    elif user==2 and computer==1:
        print("Congratulations!!You won!")
    elif user==3 and computer==2:
        print("Congratulations!!You won!")
    else:
        print("You lose!!Computer won the game!!")

    again=input("Do you want to play again?(yes/no)").lower()  #another round or not
    if again=='yes':
        start_game()
    else:
        print("Thanks for playing Rock-Paper-Scissor!")

start_game()  #Begin the game


