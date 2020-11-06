import sys
import random

def init_board():
    """Inicjuje pustą tablicę"""    
    board = []
    for i in range (0,3):
        board.append([".",".","."])
    return board

def get_move(board, player): # do naprawienia błąd jeśli drugi znak nie jest liczbą
    """pobiera od użytkownika wspłrzędne ruchu, sprawdza poprawność i zwraca ich wartość"""
    row, col = 0, 0 
    print("Podaj współrzędne na których umiescisz swój znak:",player)
    input_user = input()
    input_user = input_user.lower()
    if input_user == 'quit':
        print("Good bay !!!")
        sys.exit()
    elif len(input_user) != 2:
        print("You entered the wrong number of characters")
        get_move(board,player)
    else :        
        row = input_user[0]
        col = int(input_user[1])-1
    
    if row == "a":
        row = 0
    elif row == "b":
        row = 1
    elif row == "c":
        row = 2
        
    if input_user not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
        print("Podałeś złe współrzędne, spróbuj jeszcze raz : ")
        row,col = get_move(board, player)
    elif board[row][col] != ".":
        print("Podałeś współrzędne na których już znajduje się jakiś znak : ")
        row,col = get_move(board, player)
    
    return row, col

def mark(board, player, row, col):
    """wstawia o lub x do współrzędnych na tablicy"""
    board[row][col] = player

def has_won(board,player): #dlaczego na starcie jest False?
    "Sprawdza czy w jednej lini (poziomej, pionowej, ukośnej) występują trzy znaki, jesli tak zwraca True"
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
    """ Sprawdza czy tablica jest pełna (czy wsczystkie pola sa juz zajete)""" 
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
    """Wydruk na ekrania aktualnego stanu tablicy"""
    print("   1    2    3")
    print("A ",board[0][0],"| ",board[0][1],"| ",board[0][2])
    print("--------------")
    print("B ",board[1][0],"| ",board[1][1],"| ",board[1][2])
    print("--------------")
    print("C ",board[2][0],"| ",board[2][1],"| ",board[2][2])

def print_result(winner):
    """ Wydruk wyniku gry, kto wygrał lub remis"""
    if winner == 10:
        print("It's a tie")
    else:
        if winner%2 == 1:
            print("O has won!")
        else:
            print("X has won!")

def find_hot(board,player,hot_place):
    """Znajduje linie z  dwoma takimi samymi znakami jako szanse do ataku lub obronę"""
    for i in range (0,3):
        result =0
        temp = [[".","."]]      
        for j in range (0,3):            
            if board[i][j] == player:
                result += 1
            if board[i][j] == ".":
                temp[0] = (i,j)                
        if result == 2 and temp != [[".","."]]:
            hot_place[0] = temp[0]
            return True
            
    for i in range (0,3):        
        result =0
        temp = [[".","."]]
        for j in range (0,3):            
            if board[j][i] == player:
                result += 1
            if board[j][i] == ".":
                temp[0] = (j,i)                
        if result == 2 and temp != [[".","."]]:
            hot_place[0] = temp[0]
            return True
    
    result = 0
    temp = [[".","."]]
    for i in range (0,3):
        if board[i][i] == player:
            result += 1
        if board[i][i] == ".":
            temp[0] = (i,i)            
    if result == 2 and temp != [[".","."]]:
        hot_place[0] = temp[0]
        return True

    result = 0
    j = 2
    temp = [[".","."]]
    for i in range (0,3):
        if board[i][j] == player:
            result += 1
        if board[i][j] == ".":
            temp[0] = (i,j)            
        j -= 1
    if result == 2 and temp != [[".","."]]:
        hot_place[0] = temp[0]
        return True
    hot_place[0] = [[".","."]]  
    return False        

def tictactoe():
    """Przebieg gry"""
    board = init_board()
    option = main_menu()
    print_board(board)
    player ='x'#sprawdź czy będzie potrzebne
    user_count = 1
    
    while has_won(board, player) == False and is_full(board) == False :
        if option == 1:
            if user_count % 2 == 1:
                player = 'x'
                row,col = get_move(board, player)
            else:
                player = 'o'
                row,col = get_move(board,player)
        elif option == 2:
            if user_count % 2 == 1:
                player = 'x'
                row,col = get_move(board, player)
            else:
                player = 'o'
                row,col = get_ai_move(board,player)
        elif option == 3:
            if user_count % 2 == 1:
                player = 'x'
                row,col = get_ai_move(board, player)
            else:
                player = 'o'
                row,col = get_move(board,player)
        elif option == 4:
            if user_count % 2 == 1:
                player = 'x'
                row,col = get_move(board, player)
            else:
                player = "o"
                if board[1][1] == ".":
                    row,col = 1,1
                elif board[1][1] == "x" and user_count <= 2:
                    row, col = 0,0
                else:
                    row,col = get_ai_move(board, player)
        elif option == 5:
            if user_count % 2 == 1:
                player = 'x'
                if user_count == 1:
                    row, col = 0,0
                
                elif user_count == 3:
                    special = 0 # zmianna dla jednego ze scenariuszy który wymaga trzech kroków
                    if board[0][1] == "o" or board[1][2] == "o" or board[2][1] == "o" or board[1][0] == "o":
                        row, col = 1,1
                        special = 2
                    elif board[0][2] == "o" or board[2][2] == "o" or board[2][0] == "o":
                        if board[0][2] == ".":
                            row, col = 0,2
                            special = 1
                        else:
                            row, col = 2,0
                            special = 1
                    elif board[1][1] == "o":
                        row, col = 2,2

                elif user_count == 5 and special == 1:
                    if board[0][2] == ".":
                        row, col = 0,2
                    elif board[2][2] == ".":
                        row,col = 2,2
                    elif board[2][0] ==".":
                        row, col = 2,0
                elif user_count == 5 and special == 2:
                    row, col = 2,0
                else:
                    row,col = get_ai_move(board, player)
                
                
            else:        
                player = 'o'
                row,col = get_move(board,player)
        
        mark(board, player, row, col)
        print_board(board)
        user_count += 1
    print_result(user_count)

def get_ai_move(board,player):
    """generuje ruch komputera w zalezności od wybranych opcji"""
    good = False
    hot_place =[[".","."]]
    test_mark = player
    if find_hot(board,test_mark,hot_place) is False:
        if test_mark == "x":
            test_mark ="o"
        else :
            test_mark = "x"
        find_hot(board,test_mark,hot_place)
    while good == False:
        if hot_place[0] != [[".","."]]:
            row = int(hot_place[0][0])
            col = int(hot_place[0][1])
            good = True
        else :
            chose=[0,0]
            chose[0]=random.randint(0,2)
            chose[1]=random.randint(0,2)
            if board[chose[0]][chose[1]] == ".":
                row = int(chose[0])
                col = int(chose[1])
                good = True
            else :
                pass

    print("The computer chose: ",row,col)
    return row,col   

def main_menu():
    """Menu startowe gry"""
    state = False
    while state == False:
        while True:
            try :
                option = int(input("""
                Wybierz opcję gry :
                1 - gra dla dwóch graczy
                2 - Gracz przeciwko AI, gracz rozpoczyna (level MEDIUM)
                3 - AI przeciwko graczowi, AI rozpoczyna (level MEDIUM)
                4 - Gracz przeciwko AI - gracz rozpoczyna (level HARD - You have no chance to win)
                5 - AI przeciwko graczowi - AI rozpoczyna (level HARD - you have no chance to win, if you draw it will be your success
                """))
                break
            except ValueError :
                print("You must give a integer number")
                continue
        if option > 0 and option <= 5:
            state = True
        else:
            print("You entered a number out of range. Please try again.")
    return(option)


tictactoe()
# dopisac kontrole danych w main_menu


