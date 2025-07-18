''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

board = {'7':' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '1':' ', '2':' ', '3':' '}

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printboard(board):
    print (board['7'] +'|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print (board['4'] +'|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print (board['1'] +'|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn ='x'
    count = 0

    for i in range(10):
        printboard(board)
        print("It's your turn" + turn + "Which place will you move to?")
        move = input()

        if board[move] ==' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

# Now we will check if player X or O has won,for every move after 5 moves. 
        
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['4'] == board['5'] == board['6'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['1'] == board['2'] == board['3'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
        
            elif board['7'] == board['4'] == board['1'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['8'] == board['5'] == board['2'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['9'] == board['6'] == board['3'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['7'] == board['5'] == board['3'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
        
            elif board['9'] == board['5'] == board['1'] != ' ':
                printboard(board)
                print("\nGAME OVER!\n")
                print('*****'+turn+'*****')
                break
# If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='x':
            turn = 'O'
        else:
            turn = 'x'
    
    restart = input("DO you ant to play again?(y/n): " )
    if restart == 'y'or restart == 'Y':
        for key in board:
            board[key] = ' '

    game()

if __name__ == "__main__":
    game()
