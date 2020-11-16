board = {'TL' : ' ', 'TM' : ' ','TR' : ' ',
         'ML' : ' ', 'MM' : ' ','MR' : ' ',
         'BL' : ' ', 'BM' : ' ','BR' : ' '}

def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
    

    
turn = 'x' 
for i in range(9):
    printBoard(board)
    print ("""It's """ + turn + """'s turn. Choose a spot""" )
    move = input()
    board[move] = turn
    if turn == 'x':
        turn = '0'
    else: 
        turn = 'X'