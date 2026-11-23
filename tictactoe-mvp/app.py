#WINNING_COMBINATION
WIN_LINES =  [
   (0,1,2), (3,4,5), (6,7,8), #ROWSWC
   (0,3,6), (1,4,7), (2,5,8), #COLUMNSWC
   (0,4,8), (2,4,6)           #DIAGONALSWC
]

#BOARD
def show_board(board):
    print()
    for row in range(3):
        i = row * 3  
        a = board[i] or " " #FIRSTROW_if_empty_blankspace
        b = board[i + 1] or " " #SECONDROW_if_empty_blankspace
        c = board[i + 2] or " " #THIRDROW_if_empty_blankspace
        print(f" {a} | {b} | {c} ") #DIVIDERVERTICAL
        if row < 2 :
            print ("---+---+---")  #DIVIDERHORIZONTAL
    print()

#WINNERLINES
def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a] #WINNING_X_OR_O
    if all(cell is not None for cell in board):
        return "DRAW"
    return None #DRAW

def play():
    board = [None] * 9 
    turn = "X" #FIRST
    while True:
        show_board(board)
        move = input(f"Player {turn}, pick a cell (0-8): ").strip()

        #BOARD_SPACE_TAKEN
        if not move.isdigit(): 
                print("Type a number 0-8.")
                continue
        cell = int(move)
        if not 0 <= cell <= 8:
                print("That cell doesn't exist.")
                continue
        if board[cell] is not None:
                print("That cell is already taken.")
                continue
        board[cell] = turn    
        result = check_winner(board)
        if result == "DRAW":
                show_board(board)
                print("It's a draw!")
                break
        elif result:
                show_board(board)
                print(f"Player {result} wins!")
                break

        
        turn = "O" if turn == "X" else "X"  
    
    
if __name__ == "__main__":
     play()