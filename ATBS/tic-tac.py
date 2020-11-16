##Tic tac toe


##board data structure

board = {'top-l': ' ', 'top-m': ' ', 'top-r':' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r':' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r':' '}


## GUI display function

def printBoard(board):
    print (board['top-l'] + ' | ' + board['top-m'] + ' | ' + board['top-r'])
    print ('---------')
    print (board['top-l'] + ' | ' + board['top-m'] + ' | ' + board['top-r'])
    print ('---------')
    print (board['top-l'] + ' | ' + board['top-m'] + ' | ' + board['top-r'])

printBoard(board)
