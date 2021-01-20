playingboard = [['  ', '|', '  ', '|', '  '],['_______________________'], ['  ', '|', '  ', '|', '  '],
                ['_______________________'], ['  ', '|', '  ', '|', '  ']]



print(f'{playingboard[0]}\n{playingboard[1]}\n{playingboard[2]}\n{playingboard[3]}\n{playingboard[4]}')

possible_moves = ['top left', 'top middle', 'top right','middle left', 'middle middle', 'middle right',
                  'bottom left', 'bottom middle', 'bottom right',]
player1_moves = []
player2_moves = []
number_moves = 0

def printing_moves():
    player1_input = input("where do you want to go? (player 1)")
    while player1_input not in possible_moves or player1_input in player1_moves or player1_input in player2_moves:
        print('Put a valid number')
        player1_input = input("where do you want to go? (player 1)")
    player1_moves.append(player1_input)
    if player1_input == "top left":
        playingboard[0][0] = "X"
    elif player1_input == 'top middle':
        playingboard[0][2] = 'X'
    elif player1_input == 'top right':
        playingboard[0][4] = 'X'
    elif player1_input == 'middle left':
        playingboard[2][0] = 'X'
    elif player1_input == 'middle middle':
        playingboard[2][2] = 'X'
    elif player1_input == 'middle right':
        playingboard[2][4] = 'X'
    elif player1_input == 'bottom left':
        playingboard[4][0] = 'X'
    elif player1_input == 'bottom middle':
        playingboard[4][2] = 'X'
    elif player1_input == 'bottom right':
        playingboard[4][4] = 'X'
    print(f'{playingboard[0]}\n{playingboard[1]}\n{playingboard[2]}\n{playingboard[3]}\n{playingboard[4]}')

def printing_moves_2():
    player2_input = input("where do you want to go? (player 2)")
    while player2_input not in possible_moves or player2_input in player1_moves or player2_input in player2_moves:
        print('Put a valid number')
        player2_input = input("where do you want to go? (player 2)")
    player2_moves.append(player2_input)
    if player2_input == "top left":
        playingboard[0][0] = "o"
    elif player2_input == 'top middle':
        playingboard[0][2] = 'o'
    elif player2_input == 'top right':
        playingboard[0][4] = 'o'
    elif player2_input == 'middle left':
        playingboard[2][0] = 'o'
    elif player2_input == 'middle middle':
        playingboard[2][2] = 'o'
    elif player2_input == 'middle right':
        playingboard[2][4] = 'o'
    elif player2_input == 'bottom left':
        playingboard[4][0] = 'o'
    elif player2_input == 'bottom middle':
        playingboard[4][2] = 'o'
    elif player2_input == 'bottom right':
        playingboard[4][4] = 'o'
    else:
        print('Put a valid place')
    print(f'{playingboard[0]}\n{playingboard[1]}\n{playingboard[2]}\n{playingboard[3]}\n{playingboard[4]}')


gameover = False

while gameover == False:
    printing_moves()
    for i in range(0, 5, 2):
        if playingboard[i] == ['X', '|', 'X', '|', 'X']:
            print("Player one is the winner")
            exit()
    for i in range(0, 5, 2):
        if playingboard[0][i] == 'X' and playingboard[2][i] == 'X' and playingboard[4][i] == 'X':
            print('player one is the winner')
            exit()
    if playingboard[0][0] == 'X' and playingboard[2][2] == 'X' and playingboard[4][4] == 'X':
        print('player one is the winner')
        exit()
    if playingboard[0][4] == 'X' and playingboard[2][2] == 'X' and playingboard[4][0] == 'X':
        print('player one is the winner')
        exit()
    number_moves += 1
    if number_moves >= 9:
        print('tie')
        break
    printing_moves_2()
    for i in range(0, 5, 2):
        if playingboard[i] == ['o', '|', 'o', '|', 'o']:
            print("Player two is the winner")
            exit()
    if playingboard[0][0] == 'o' and playingboard[2][2] == 'o' and playingboard[4][4] == 'o':
        print('player two is the winner')
        exit()
    if playingboard[0][4] == 'o' and playingboard[2][2] == 'o' and playingboard[4][0] == 'o':
        print('player two is the winner')
        exit()
    number_moves += 1
    if number_moves >= 9:
        print('tie')
        break
