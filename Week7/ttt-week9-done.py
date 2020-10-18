import turtle

def convert(x, y):
    return 3*y + x

# Now after we click, we want to track status
# There are two status we want to track
# One is whose turn is it now?
# The other status is the board_status

turn = 'X'
board_status = [''] * 9

def draw_turn(pen, turn, x, y):
    pen.goto(x, y)
    pen.pendown()
    pen.write(turn, align='center', font=('Arial', 80, 'normal'))
    pen.penup()

def winner(status_3_pieces):
    if (status_3_pieces[0] == status_3_pieces[1] == status_3_pieces[2]):
        return status_3_pieces[0]
    return ''

def who_is_winner(board_status):
    possibilities = [
        [board_status[2], board_status[4], board_status[6]],
        [board_status[0], board_status[4], board_status[8]]
    ]
    for i in range(3):
        possibilities.append(board_status[3*i:3*i+3])
        possibilities.append(board_status[i:9:3])
        
    for status in possibilities:
        winner_cand = winner(status)
        if winner_cand != '':
            return winner_cand
    return ''

def click(x, y): 
    global pen, turn, screen, board_status
    if x >= 0 and x < 30 and y >= 0 and y < 30:
        board_x = int(x) // 10
        board_y = int(y) // 10
        print('Clicked: ', board_x, board_y, " index", convert(board_x, board_y), " turn:", turn)

        if board_status[convert(board_x, board_y)] == '':
            draw_turn(pen, turn, board_x * 10 + 5, board_y * 10 + 2.5)
            board_status[convert(board_x, board_y)] = turn
            if turn == 'X':
                turn = 'O'
            elif turn == 'O':
                turn = 'X'

            if who_is_winner(board_status) != '':
                print("Winner is ", who_is_winner(board_status))
                screen.onclick(None)               
                
        print(board_status)

screen = turtle.Screen() 
screen.title('Tic-Tac-Toe') 
screen.setworldcoordinates(-5, -5, 35, 35)
screen.onclick(click)

pen = turtle.Turtle() 
 
for i in range(0, 4): 
    pen.penup() 
    pen.speed(0) 
    pen.goto(0, i*10) 
    pen.pendown() 
    pen.speed(0) 
    pen.forward(30) 
 
pen.left(90) 
 
for i in range(0, 4): 
    pen.penup() 
    pen.speed(0) 
    pen.goto(i*10, 0) 
    pen.pendown() 
    pen.forward(30) 
 
pen.penup()
 
screen.mainloop()
