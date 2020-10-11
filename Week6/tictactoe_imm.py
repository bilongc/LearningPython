import turtle

def convert(x, y):
    return 3*y + x

def click(x, y): 
    global click_count, pen, turn, screen
    board_x = int(x) // 10
    board_y = int(y) // 10
    print('Clicked: ', board_x, board_y, " index", convert(board_x, board_y)) 

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
