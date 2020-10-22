def init_board():
    board = []
    for i in range (0,3):
        board.append([".",".","."])
    return board

def get_move(board, player): # do naprawienia błąd jeśli drugi znak nie jest liczbą
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0 
    print("Podaj współrzędne na których umiescisz swój znak:",player)
    input_user = input()
    input_user = input_user.lower()
    if len(input_user) != 2:
        print("Podałeś niewłaściwą ilość znaków")
        get_move(board,player)
    else :
        
        row = input_user[0]
        col = int(input_user[1])
    
    if row == "a":
        row = 0
    elif row == "b":
        row = 1
    elif row == "c":
        row = 2
    else:
        pass
    
    if input_user not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
        print("Podałeś złe współrzędne, spróbuj jeszcze raz : ")
        get_move(board,player)
    elif board[row][col-1] != ".":
        print("Podałeś współrzędne na których już znajduje się jakiś znak : ")
        get_move(board,player)
    else:
        pass
    return row, col

def mark(board, player, row, col):
    
    board[row][col-1] = player

def has_won(board,player): #dlaczego na starcie jest False?
    
    for i in range (0,3):
        result =0
        for j in range (0,3):
            if board[i][j] == player:
                result += 1
            if result == 3:
                return True
            
    for i in range (0,3):
        result =0
        for j in range (0,3):
            if board[j][i] == player:
                result += 1
            if result == 3:
                return True
    result = 0
    for i in range (0,3):
        if board[i][i] == player:
            result += 1
        if result == 3:
                return True
    result = 0
    j = 2
    for i in range (0,3):
        if board[i][j] == player:
            result += 1
        if result == 3:
            return True
        j -= 1
    return False

def is_full(board):
    full = 0
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j] == 'x' or board[i][j] == 'o':
                full+= 1
    if full == 9:
        return True
    else:
        return False

def print_board(board):
    print("   1    2    3")
    print("A ",board[0][0],"| ",board[0][1],"| ",board[0][2])
    print("--------------")
    print("B ",board[1][0],"| ",board[1][1],"| ",board[1][2])
    print("--------------")
    print("C ",board[2][0],"| ",board[2][1],"| ",board[2][2])

def print_result(winner):
    
    if winner == 10:
        print("It's a tie")
    else:
        if winner%2 == 1:
            print("O has won!")
        else:
            print("X has won!")
        

def tictactoe():
    board = init_board()
    print_board(board)
    player ='x'
    user_count = 1
    while has_won(board, player) == False and is_full(board) == False :
        if user_count%2 == 1:
            player = 'x'
        else:
            player = 'o'
        row,col = get_move(board, player)
        mark(board, player, row, col)
        print_board(board)
        user_count += 1
    print_result(user_count)



tictactoe()

# board = init_board()
# row,col = get_move(board, player)
# mark(board, player, row, col)
# if has_won(board,player):
#     print("wygrałeś")
# print_board(board)

