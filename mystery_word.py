import random

def create_board(word):
    board_list = []
    for letter in word:
        board_list.append("_")
    print(f"Here is your word to guess: {' '.join(board_list)}")
    return board_list

def show_board(word, board, correct_list):
    for letter in correct_list:
        for idx in range(len(word)):
            if word[idx] == letter:
                board[idx] = letter
    print(" ".join(board))

def get_user_guess():
    guess = input("Guess a letter: ")
    return guess

def play_game():
    # computer picks a word at random from the list
    # start with one word
    # TODO pick word from list
    word_to_guess = 'dream'.upper()

    # let user know length of secret word. make the board showing blanks for letters.
    game_board = create_board(word_to_guess)
    correct_guesses = []
    incorrect_guesses = []
    #show_board(word_to_guess)

    while len(incorrect_guesses) < 8 and "_" in game_board:
        new_guess = get_user_guess().upper()
        if new_guess in word_to_guess:
            correct_guesses.append(new_guess)
        else:
            incorrect_guesses.append(new_guess)
        show_board(word_to_guess, game_board, correct_guesses)
        print(f"Incorrect letters: {' '.join(incorrect_guesses)}")

    if len(incorrect_guesses) == 8:
        print("You LOSE!")
    else:
        print("You WIN!")




if __name__ == "__main__":
    play_game()
