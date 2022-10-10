    
def create_board(word):
    board_list = []
    for letter in word:
        board_list.append("_")
    print(f"Here is your word to guess: {' '.join(board_list)}")
    return board_list

#def show_board(word):
    #TODO display


def get_user_guess():
    guess = input("Guess your letter: ")
    print(guess)
    return guess

def play_game():
    # computer picks a word at random from the list
    # start with one word
    # TODO pick word from list
    word_to_guess = 'dream'

    # let user know length of secret word. make the board showing blanks for letters.
    game_board = create_board(word_to_guess)
    correct_guesses = []
    incorrect_guesses = []
    #show_board(word_to_guess)
    new_guess = get_user_guess()





if __name__ == "__main__":
    play_game()
