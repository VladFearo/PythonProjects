def display_board(board):
    """
    displays the board of the game
    :param board: a list of strings
    :return: None
    """
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])


def player_input(board):
    """
    takes the choices of X or O from player 1 and gives the other option to player2
    :param board: a list of strings
    :return: None
    """
    player1_choice = 'Wrong'
    while player1_choice not in ['X', 'O']:
        player1_choice = input('Player1 Choose X or O:')
        if player1_choice not in ['X', 'O']:
            print('Invalid choice, try again.')
        if player1_choice == 'X':
            player2_choice = 'O'
        else:
            player2_choice = 'X'
    play(board, player1_choice, player2_choice)


def play(board, player1_choice, player2_choice):
    """
    the gameplay logic of TicTacToe
    :param board: a list of strings
    :param player1_choice: a string of 'X' or 'O'
    :param player2_choice: a string of 'X' or 'O'
    :return: None
    """
    while not end_game(board):
        player_choice = -1
        occupied = False
        while player_choice not in range(1, 9) or occupied:
            display_board(board)
            player_choice = int(input(f"Player1 choose where to put {player1_choice} (1-9):"))
            if board[player_choice] == ' ':
                board[player_choice] = player1_choice
                occupied = False
            else:
                occupied = True
                print("Error the space is already occupied")
        display_board(board)
        if win(board, player1_choice, player2_choice) or end_game(board):
            return
        player_choice = -1
        occupied = True
        while player_choice not in range(1, 9) or occupied:
            player_choice = int(input(f"Player2 choose where to put {player2_choice} (1-9):"))
            if board[player_choice] == ' ':
                board[player_choice] = player2_choice
                occupied = False
            else:
                occupied = True
                print("Error the space is already occupied")
        display_board(board)
        if win(board, player1_choice, player2_choice) or end_game(board):
            return


def end_game(board):
    """
    checks to see if the board has reached an end game where all the squares are occupied.
    :param board: a list of strings
    :return: boolean
    """
    counter = 0
    for i in board:
        if i in ['X', 'O']:
            counter += 1
    if counter == 9:
        print("Its a tie!")
        return True
    else:
        return False


def win(board, player1_choice, player2_choice):
    """
    checks all the options for both players to see if they have a winning position
    :param board: a list of strings
    :param player1_choice: a string of 'X' or 'O'
    :param player2_choice: a string of 'X' or 'O'
    :return: boolean
    """
    if board[1] == player1_choice and board[2] == player1_choice and board[3] == player1_choice:
        print("Player1 Win!")
        return True
    if board[1] == player2_choice and board[2] == player2_choice and board[3] == player2_choice:
        print("Player2 Win!")
        return True
    if board[4] == player1_choice and board[5] == player1_choice and board[6] == player1_choice:
        print("Player1 Win!")
        return True
    if board[4] == player2_choice and board[5] == player2_choice and board[6] == player2_choice:
        print("Player2 Win!")
        return True
    if board[7] == player1_choice and board[8] == player1_choice and board[9] == player1_choice:
        print("Player1 Win!")
        return True
    if board[7] == player2_choice and board[8] == player2_choice and board[9] == player2_choice:
        print("Player2 Win!")
        return True
    if board[1] == player1_choice and board[4] == player1_choice and board[7] == player1_choice:
        print("Player1 Win!")
        return True
    if board[1] == player2_choice and board[4] == player2_choice and board[7] == player2_choice:
        print("Player2 Win!")
        return True
    if board[2] == player1_choice and board[5] == player1_choice and board[8] == player1_choice:
        print("Player1 Win!")
        return True
    if board[2] == player2_choice and board[5] == player2_choice and board[8] == player2_choice:
        print("Player2 Win!")
        return True
    if board[3] == player1_choice and board[6] == player1_choice and board[9] == player1_choice:
        print("Player1 Win!")
        return True
    if board[3] == player2_choice and board[6] == player2_choice and board[9] == player2_choice:
        print("Player2 Win!")
        return True
    if board[1] == player1_choice and board[5] == player1_choice and board[9] == player1_choice:
        print("Player1 Win!")
        return True
    if board[1] == player2_choice and board[5] == player2_choice and board[9] == player2_choice:
        print("Player2 Win!")
        return True
    if board[3] == player1_choice and board[5] == player1_choice and board[7] == player1_choice:
        print("Player1 Win!")
        return True
    if board[3] == player2_choice and board[5] == player2_choice and board[7] == player2_choice:
        print("Player2 Win!")
        return True
    return False


def main():
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)

    while True:
        player_input(board)
        play_again = "Error"
        while play_again not in ["Y", "N"]:
            play_again = input("Play again? Y/N: ")
            if play_again not in ["Y", "N"]:
                print("Wrong input entered! try again.")
        if play_again == 'N':
            break


if __name__ == "__main__":
    main()
