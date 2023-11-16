symbols = ["X", "O"]
currentPlayer = symbols[0]
default_board = [" " for i in range(9)]
gameRunning = True


def drawBoard(board):
    print("+---" * 3 + "+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---" * 3 + "+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---" * 3 + "+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---" * 3 + "+")


def getPlayerMove(board):
    global currentPlayer
    global gameRunning
    print(f"{currentPlayer}, it is your turn.")
    move = int(input("Choose a square for your move (1-9): \n"))
    if 1 <= move <= 9 and board[move - 1] == " ":
        board[move - 1] = currentPlayer
    elif board[move - 1] != " ":
        print("That square is occupied.")
    else:
        print("You entered an invalid input or that square is occupied.")


def checkForWin(board):
    global gameRunning
    if checkHorizontal(board, 0) or checkHorizontal(board, 3) or checkHorizontal(board, 6):
        drawBoard(board)
        print(f"{currentPlayer} wins!")
        gameRunning = False
    elif checkVertical(board, 0) or checkVertical(board, 1) or checkVertical(board, 2):
        drawBoard(board)
        print(f"{currentPlayer} wins!")
        gameRunning = False
    elif checkDiagonal(board):
        drawBoard(board)
        print(f"{currentPlayer} wins!")
        gameRunning = False


def checkHorizontal(current_board, start_index):
    if current_board[start_index] == current_board[start_index + 1] == current_board[start_index + 2] == currentPlayer:
        return True


def checkVertical(current_board, start_index):
    if current_board[start_index] == current_board[start_index + 3] == current_board[start_index + 6] == currentPlayer:
        return True


def checkDiagonal(current_board):
    if current_board[0] == current_board[4] == current_board[8] == currentPlayer:
        return True
    elif current_board[2] == current_board[4] == current_board[6] == currentPlayer:
        return True


def checkForTie(current_board):
    global gameRunning
    if " " not in current_board:
        drawBoard(current_board)
        print("Game ends in a tie.")
        gameRunning = False


def switchSides():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = symbols[1]
    else:
        currentPlayer = symbols[0]


def main():
    board = default_board
    print("Welcome to Tic-Tac-Toe of Death!!!")
    print("Squares start at 1 at the top left and end at 9 in the bottom right.")
    while gameRunning:
        drawBoard(board)
        getPlayerMove(board)
        checkForWin(board)
        checkForTie(board)
        switchSides()


main()
