import turtle 
 
screen = turtle.Screen() 
screen.title('Tic-Tac-Toe') 
screen.setworldcoordinates(-5, -5, 35, 35) 
 
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
 
for i in range(4): 
    x = eval(input("Enter x coordinate for X's move: ")) 
    y = eval(input("Enter y coordinate for X's move: ")) 
    pen.goto(x*10+5, y*10+2.5) 
    pen.write("X", align='center', font=('Arial', 80, 'normal')) 
    x = eval(input("Enter x coordinate for X's move: ")) 
    y = eval(input("Enter y coordinate for X's move: ")) 
    pen.goto(x*10+5, y*10+2.5) 
    pen.write("O", align='center', font=('Arial', 80, 'normal')) 
 
pen.goto(-2.5, -2.5) 
pen.write("Thank you for playing!", font=('Arial', 20, 'normal')) 
