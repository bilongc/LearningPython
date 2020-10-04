import turtle 
import math 
 
turn = 'X' 
states = [''] * 9 
 
def has_winner(pieces): 
    if pieces[0] == pieces[1] == pieces[2]: 
        return pieces[0] 
    else: 
        return '' 
 
def who_is_winner(states): 
    for i in range(3): 
        winner = has_winner(states[i*3:(i+1)*3]) 
        if winner != '': 
            return winner 
    for i in range(3): 
        winner = has_winner(states[i:9:3]) 
        if winner != '': 
            return winner 
    diagonals = [[states[0], states[4], states[8]], 
                 [states[2], states[4], states[6]]] 
    for i in range(len(diagonals)): 
        winner = has_winner(diagonals[i]) 
        if winner != '': 
            return winner 
    return '' 
 
def click(x, y): 
    global click_count, pen, turn, screen 
    print('Clicked: ', x, y) 
    board_x = int(x // 100) 
    board_y = int(y // 100) 
    if board_x >= 0 and board_y <= 2 and board_y >= 0 and board_y <= 2: 
        if turn == 'X': 
            draw_cross(pen, board_x, board_y) 
            states[board_y * 3 + board_x] = 'X' 
            turn = 'O' 
        else: 
            draw_nought(pen, board_x, board_y) 
            states[board_y * 3 + board_x] = 'O' 
            turn = 'X' 
    winner = who_is_winner(states) 
    if winner != '': 
        screen.onclick(None) 
        pen.goto(-25, -25) 
        pen.seth(0) 
        pen.write("Thank you for playing! Winner is: {}".format(winner), font=('Arial', 20, 'normal')) 
        print("Winner is ", winner) 
 
 
def draw_line(pen, start_x, start_y, heading, length): 
    pen.penup() 
    pen.goto(start_x, start_y) 
    pen.seth(heading) 
    pen.pendown() 
    pen.forward(length) 
    pen.penup() 
     
def draw_boundary(pen, heading): 
    for i in range(0, 4): 
        if heading == 90: 
            goto_x = i * 100 
            goto_y = 0 
        else: 
            goto_x = 0 
            goto_y = i * 100 
        draw_line(pen, goto_x, goto_y, heading, 300) 
 
def draw_board(pen): 
    draw_boundary(pen, 0) 
    draw_boundary(pen, 90) 
 
def draw_cross(pen, board_x, board_y): 
    goto_x = board_x * 100 + 10 
    goto_y = board_y * 100 + 10 
    draw_line(pen, goto_x, goto_y, 45, math.sqrt(2) * 80) 
    goto_x = board_x * 100 + 10 
    goto_y = (board_y + 1) * 100 - 10 
    draw_line(pen, goto_x, goto_y, -45, math.sqrt(2) * 80) 
 
def draw_nought(pen, board_x, board_y): 
    goto_x = board_x * 100 + 90 
    goto_y = board_y * 100 + 50 
    pen.penup() 
    pen.goto(goto_x, goto_y) 
    pen.seth(90) 
    pen.pendown() 
    pen.circle(40) 
 
screen = turtle.Screen() 
screen.title('Tic-Tac-Toe') 
screen.setworldcoordinates(-50, -50, 350, 350) 
screen.onclick(click) 
 
pen = turtle.Turtle() 
pen.speed(0) 
draw_board(pen) 
 
screen.mainloop() 
 
