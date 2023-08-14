import random

valid_calls = ['rock','paper','scissors','spock','lizard']

def get_user_choice():
    choice = input("Enter your move: ")
    return choice.lower()

def get_computer_choice():
    choice = random.choice(valid_calls)
    return choice

def determine_winner(user_choice,computer_choice):

    if user_choice == computer_choice:
        print('Computer\'s Choice: ',computer_choice)
        return ('Same move, please pick another move')

    elif user_choice == 'rock':
        print('Computer\'s Choice: ',computer_choice)
        if computer_choice == 'scissors':
            return ('Rock crushes scissors, YOU WIN!')
        elif computer_choice == 'lizard':
            return ('Rock crushes lizard, YOU WIN!')
        else:
            if computer_choice == 'paper':
                return ('Paper covers rock, YOU LOSE!')
            elif computer_choice == 'spock':
                return ('Spock vaporizes rock, YOU LOSE!')
                

    elif user_choice == 'scissors':
        print('Computer\'s Choice: ',computer_choice)
        if computer_choice == 'paper':
            return ('Scissors cut paper, YOU WIN!')
        elif computer_choice == 'lizard':
            return ('Scissors decapitate lizard, YOU WIN!')
        else:
            if computer_choice == 'rock':
                return ('Rock crushes scissors, YOU LOSE!')
            elif computer_choice == 'spock':
                return ('Spock smashes scissors, YOU LOSE!')
        
    elif user_choice == 'paper':
        print('Computer\'s Choice: ',computer_choice)
        if computer_choice == 'rock':
            return ('Paper covers rock, YOU WIN!')
        elif computer_choice == 'spock':
            return ('Paper disproves spock, YOU WIN!')
        else:
            if computer_choice == 'scissors':
                return ('Scissors cut paper, YOU LOSE!')
            elif computer_choice == 'lizard':
                return ('Lizard eats paper, YOU LOSE!')

    elif user_choice == 'lizard':
        print('Computer\'s Choice: ',computer_choice)
        if computer_choice == 'spock':
            return ('Lizard poisons spock, YOU WIN!')
        elif computer_choice == 'paper':
            return ('Lizard eats paper, YOU WIN!')
        else:
            if computer_choice == 'rock':
                return ('Rock crushes lizard, YOU LOSE!')
            elif computer_choice == 'scissors':
                return ('Scissors decapitate lizard, YOU LOSE!')
        
    elif user_choice == 'spock':
        print('Computer\'s Choice: ',computer_choice)
        if computer_choice == 'rock':
            return ('Spock vaporizes rock, YOU WIN!')
        elif computer_choice == 'scissors':
            return ('Spock smashes scissors, YOU WIN!')
        else:
            if computer_choice == 'paper':
                return ('Paper disproves spock, YOU LOSE!')
            elif computer_choice == 'lizard':
                return ('Lizard poisons spock, YOU LOSE!')
            
    elif user_choice == 'quit':
        return 'SCORE BOARD: '
    
    elif user_choice not in valid_calls:
        return ('Invalid move, please enter: rock,paper,scissors,lizard or spock!')

def final_scores(computer_wins,user_wins,ties):
    print('Your number of wins: ',user_wins)
    print('Computer\'s number of wins: ',computer_wins)
    print('Number of draws: ',ties)

    if user_wins > computer_wins:
        print('YOU DEFEATED THE COMPUTER!')
    elif computer_wins == user_wins:
        print('IT IS A DRAW, SCORE :',ties)
    else:
        print('THE COMPUTER WINS!')