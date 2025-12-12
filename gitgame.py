# This is my git game a tic tac toe my friend

board = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']
]

def display_board():
    for row in board:
        print(' | '.join(row))
        print('---------')

def get_move():
    move = input('Enter Move: ').split()
    row = int(move[0])
    col = int(move[1])
    return row, col



player = True

display_board()

while True:
    r, c =  get_move()

    board[r-1][c-1] = 'X' if player else 'O'


    display_board() 

    player = not player








