import turtle

def convert(x, y):
    return 3*y + x

# Now after we click, we want to track status
# There are two status we want to track
# One is whose turn is it now?
# The other status is the board_status

turn = 'X'
board_status = [''] * 9

def click(x, y): 
    global pen, turn, screen, board_status
    if x >= 0 and x < 30 and y >= 0 and y < 30:
        board_x = int(x) // 10
        board_y = int(y) // 10
        print('Clicked: ', board_x, board_y, " index", convert(board_x, board_y), " turn:", turn)
        
        if turn == 'X':
            turn = 'O'
            board_status[convert(board_x, board_y)] = 'X'
        elif turn == 'O':
            turn = 'X'
            board_status[convert(board_x, board_y)] = 'O'
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
