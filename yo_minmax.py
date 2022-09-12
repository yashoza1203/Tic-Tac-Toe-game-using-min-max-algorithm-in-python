global player,bot
moves=['O','X']
Tic_Tac_toe_Board={'top-L':'1','top-M':'2','top-R':'3',
                   'mid-L':'4','mid-M':'5','mid-R':'6',
                   'bot-L':'7','bot-M':'8','bot-R':'9'}

mylist=[['top-L','top-M','top-R'],
        ['mid-L','mid-M','mid-R'],
        ['bot-L','bot-M','bot-R']]

yolist=['top-L','top-M','top-R',
        'mid-L','mid-M','mid-R',
        'bot-L','bot-M','bot-R']

Win_moves=[[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]

def evaluate():
    for list in Win_moves:
        a,b,c=list
        if Tic_Tac_toe_Board[yolist[a]] == Tic_Tac_toe_Board[yolist[b]] == Tic_Tac_toe_Board[yolist[c]]==bot:
            return 10
        elif Tic_Tac_toe_Board[yolist[a]] == Tic_Tac_toe_Board[yolist[b]] == Tic_Tac_toe_Board[yolist[c]]==player:
            return -10

def findbestmove():
    bestVal=-10
    bestMove=0
    for yo in yolist:
        if Tic_Tac_toe_Board[yo] not in moves:
            num=Tic_Tac_toe_Board[yo]
            Tic_Tac_toe_Board[yo]=bot
            moveVal=minimax(Tic_Tac_toe_Board,0,False)
            print('moveval',moveVal)
            Tic_Tac_toe_Board[yo] = num
            if (moveVal > bestVal):			
                bestMove = yo
                bestVal = moveVal
    return bestMove

def minimax(Tic_Tac_toe_Board,depth,isMax):
    score = evaluate()
    if (score == 10) :
        return score
    if (score == -10) :
        return score
    elif checkdraw():
        return 0
    if (isMax):
        best=-1000
        for yo in yolist:
            if Tic_Tac_toe_Board[yo] not in moves:
                num =Tic_Tac_toe_Board[yo]
                Tic_Tac_toe_Board[yo]=bot
                best=max(best,minimax(Tic_Tac_toe_Board,depth+1,False))
                Tic_Tac_toe_Board[yo] = num
        return best
    else:
        best=1000
        for yo in yolist:
            if Tic_Tac_toe_Board[yo]  not in moves:
                num =Tic_Tac_toe_Board[yo]
                Tic_Tac_toe_Board[yo]=player
                best=min(best,minimax(Tic_Tac_toe_Board,depth+1,True))
                Tic_Tac_toe_Board[yo] = num
        return best

def checkdraw():
    drawcount=0
    for list in mylist:
        if Tic_Tac_toe_Board[list[0]] and Tic_Tac_toe_Board[list[1]] and Tic_Tac_toe_Board[list[2]] in moves:
            drawcount+=1
    if drawcount==3:
        return True
    else:
        return False

        
def PrintBoard(board):
    count=0
    board_count=0
    for list in mylist:
        print(board[list[count]]+'| '+board[list[count+1]]+' | '+board[list[count+2]])
        if board_count<=1:        
            print('-+ - +-')
        board_count+=1
        print()

def winner():
    if evaluate()==-10:
        print('player won')
        exit()
    elif evaluate()==10:
        print('bot won')
        exit()
    else:
        if checkdraw()==True:
            print('its a DRAW')
            exit()
            
flag=0
PrintBoard(Tic_Tac_toe_Board)

def player_move(inp):
    if Tic_Tac_toe_Board[yolist[inp-1]] not in moves:
        Tic_Tac_toe_Board[yolist[inp-1]]=player
    else:
        print('Cell occupied try again :-)')
        inp=int(input('Enter the square no. player :'))
        player_move(inp)

def bot_move(inp):
        Tic_Tac_toe_Board[inp]=bot
player=input('Enter what u want to choose X or O?')
player=player.upper()

if player=='X':
    bot='O'
else:
    bot='X'

for i in range(2,11):
    if i%2==0:
        if player == 'X':
            inp=int(input('Enter the square no. player:'))
            player_move(inp)
        elif bot == 'X':
            inp=findbestmove()
            print(inp)
            bot_move(inp)
    else:
        if player == 'O':
            inp=int(input('Enter the square no. player:'))
            player_move(inp)
        elif bot=='O':
            inp=findbestmove()
            print(inp)
            bot_move(inp)
    
    PrintBoard(Tic_Tac_toe_Board)
    winner()