from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)
print "You get 4 chances to guess where my ship is located."

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#Used to find ship location in debugging
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", turn + 1

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row-1][guess_col-1] == "X"):
            print "You guessed that one already."
        else:
            if turn == 3:
                print "Game Over"
                exit(0)
            else:
                print "You missed my battleship!"
                board[guess_row-1][guess_col-1] = "X"
    # Print (turn + 1) here!
            print_board(board)
