import turtle
import time
import random

# Step 1: Create a screen, and configure the screen
screen = turtle.Screen()
screen.title("Snake")
screen.setup(width=600, height=600)

# Step 2.1: Create food and configure the food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

# Step 2.2: Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('yellow')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Step 3: Code the snake head to move up and down
def move_up():
    if head.direction != "down":
        head.direction = "up"
        
    print("snake is moving up")

def move_down():
    if head.direction != "up":
        head.direction = "down"

    print("snake is moving down")

def move_left():
    if head.direction != "right":
        head.direction = "left"

    print("snake is moving left")

def move_right():
    if head.direction != "left":
        head.direction = "right"

    print("snake is moving right")

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_right, "Right")

body = []
delay = 0.2

while True:
    if abs(head.xcor()) >= 300 or abs(head.ycor()) >= 300:
        head.direction = "stop"
        head.goto(0, 0)
        food.goto(0, 100)

        for t in body:
            t.clear()
            t.hideturtle()
            
        body = []
        
    screen.update()
    
    if head.distance(food) < 20:
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape('square')
        tail.color('blue')
        tail.penup()
        body.append(tail)
        goto_x = random.randint(-300, 300)
        goto_y = random.randint(-300, 300)
        food.goto(goto_x, goto_y)

    if len(body) > 0:
        body[-1].goto(head.xcor(), head.ycor())
        body = body[-1:] + body[0:-1]
    
    move()

    time.sleep(delay)

screen.mainloop()
