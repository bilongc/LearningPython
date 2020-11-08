import turtle
import time

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
delay = 1

while True:
    screen.update()
    
    if head.distance(food) < 20:
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape('square')
        tail.color('blue')
        tail.penup()
        body.append(tail)

    move()

    time.sleep(delay)

screen.mainloop()
