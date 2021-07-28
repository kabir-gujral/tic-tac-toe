# Tic - Tac - Toe

from random import shuffle
from os import system

def drawBoard(board):
    system("cls")
    print()
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")


# board = [' ','X','O','O'," "," ",' ','X',' ']

board=[" "]*9
p1_marker=None
p2_marker=None
def reset():
    global p1_marker,p2_marker,board


    symbols = ['O','X']

    shuffle(symbols)

    p1_marker,p2_marker = symbols 
    board = [' ']*9


turn = 'X'

drawBoard(board)

def takeInput(marker):
    pos = int(input("Enter the position: "))

    if board[pos-1]==" ":
        board[pos-1]=marker
    elif board[pos-1]!=" ":
        print("position already occupied ")
        takeInput(marker)


def checkDraw(board):
    if board.count(" ")==0:
        return True 
    return False

def gameplay(marker):  
    takeInput(marker)
    drawBoard(board) 

win_triplets = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
score1 = 0
score2 = 0

def winCheck(board,marker):
    global score1,score2
    result = list(filter(lambda a:board[a[0]]==board[a[1]]==board[a[2]]==marker,win_triplets))
    if len(result)>0:
        print(marker,"Won the game")
        if p1_marker==marker:
           score1+=1
        else:
           score2+=1
        return True
    return False
reset()
while True:   
    print(f"player 1 score {score1}-----------player 2 score {score2} ")
        
    while True:
        if turn==p1_marker:
            gameplay(p1_marker)
        else:
            gameplay(p2_marker)
            
        if winCheck(board,turn):
            
            

            break
            
        if checkDraw(board):
            print("game drawn")
            break

        turn = p1_marker if turn==p2_marker else p2_marker
    
    playagain=input("do you want to play again")
    if playagain=="yes":
        reset()       
    else:
        break
