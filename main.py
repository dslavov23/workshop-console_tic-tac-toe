def read_players():
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()
    while player_one_sign not in ['X', 'O']:
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    player_two_sign = 'O' if player_one_sign == 'X' else 'X'
    return [(player_one_name, player_one_sign), (player_two_name, player_two_sign)]


def print_board_numeration(board):
    print('This is the numeration of the board:')
    idx = 1
    for row in range(len(board)):
        print('|', end='')
        for col in range(len(board)):
            print(f'  {idx:02d}  |', end='')
            idx += 1
        print()


def play_game(players, board):
    print(f'{players[0][0]} starts first!')
    while True:
        player_name, player_sign = players[0]
        position = int(input(f'{player_name} choose a free position [1-{len(board) * len(board)}]: '))
        players[0], players[1] = players[1], players[0]


players = read_players()

board_size = 3
board = []
[board.append([None] * board_size) for _ in range(board_size)]

print_board_numeration(board)

play_game(players, board)