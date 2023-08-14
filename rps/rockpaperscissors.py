from functions.functions import*

def play_game():
    user_choice = ''
    user_win_count = 0
    computer_win_count = 0
    tie_count = 0

    while user_choice != 'quit':
        the_user_choice = get_user_choice()
        the_computer_choice = get_computer_choice()
        winner = determine_winner(the_user_choice,the_computer_choice)
        print(winner)

        if 'WIN' in winner:
            user_win_count+=1
        elif 'LOSE' in winner:
            computer_win_count+=1
        elif 'another move' in winner:
            tie_count+=1
        
        if the_user_choice  == 'quit':
            final_scores(user_win_count,computer_win_count,tie_count)
            print('GAME OVER!')
            break
    
if __name__ == "__main__":
    play_game()

        