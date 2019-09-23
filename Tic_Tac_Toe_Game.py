###############################     Tic Tac Toe Game    #############################

from itertools import cycle

def win(current_game):

    def all_same(L):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in game:
        print(row)
        if all_same(row):  # Horizontals the same? win
            print(f"Player {row[0]} is the winner horizontally(-)")
            return True
 
    diags = []
    for col, row, in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags): 
           print(f"Player {diags[0]} is the winner diagonally(/)")
           return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags): 
           print(f"Player {diags[0]} is the winner diagonally(\\)")
           return True

    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])   # verticles the same? win 
        if all_same(check):
             print(f"Player {check[0]} is the winner vertically(|)")
             return True
    return False  # nobody won

def game_board(game_map, player = 0, row = 0, col = 0, just_display = False):
    try:
        if game_map[row][col] != 0:
            print("Position Taken, choose another! ")
            return game_map, False
        print("   0  1  2")

        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map, start = 0):
            print(count, row)
        print("\n") 
        return game_map, True

    except IndexError as e:
        print("Did you input row/col as 0, 1, or 2", e)
        return game_map, False

    except Exception as e:
        print("Fatel Error - Something went very wrong", e)
        return game_map, False

play = True
player_choice = cycle([1,2])  # iterator -> itertool.cycle()
while play:
    game = [[0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0],] 

    game_won = False
    game, _ = game_board(game, just_display = True)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player} ")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2) "))
            row_choice    = int(input("What row do you want to play? (0, 1, 2) "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Play again? (y/n) ")
            if again.lower() == "y":
                print("OK")
            elif again.lower() == "n":
                print("Goodbye!!")
                play = False
            else:
                print("Invalid Input - Bye")
                play - False
            