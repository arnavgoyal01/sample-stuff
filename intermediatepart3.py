game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def new_gameboard(row, column:
gameboard = []
row = []
int i, j

def game_board(p ayer=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)


game_board()
game_board(player=2, row=0, column=0)
