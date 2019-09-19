from turtle import *
import random

bg = Screen()
bg.screensize(300,300)
snake = Turtle()
snake.penup()
snake.speed(0)
snake.shape("square")

food = Turtle()
food.hideturtle()
food.penup()
food.shape("circle")
food.color("red")

foodExists = False
foodLocation = (None, None)
length = 3
history = []

def gameOver():
    food.clearstamps(1)
    snake.clearstamps(1)
    history.pop()    
    if history:
        bg.ontimer(gameOver, 300)
    else:
        bg.delay(300)
        snake.hideturtle()
        snake.goto(140, 190)
        snake.color("red")
        snake.write("You Lose", False, align = "center", font=("Comic Sans", 50, "bold"))

def foodSpawn():
    global foodExists
    global foodLocation

    randX, randY = 30 * random.randint(-9,9), 30 * random.randint(-8,8)
    while (randX, randY) in history:
        randX, randY = 30 * random.randint(-9,9), 30 * random.randint(-8,8)
        
    food.setpos(randX, randY)
    food.stamp()
    foodExists = True
    foodLocation = eval(str(food.pos()))

def screenTravel(turtle, position):
    if position[0] > 300:
        position = (-300 , position[1])
        snake.goto(position[0], position[1])

    if position[0] < -300:
        position = (300 , position[1])
        snake.goto(position[0], position[1])

    if position[1] > 240:
        position = (position[0], -240)
        snake.goto(position[0], position[1])

    if position[1] < -240:
        position = (position[0], 240)
        snake.goto(position[0], position[1])

    return(position)


    
def travel():
    global length
    global foodLocation
    global foodExists

    snake.forward(30)
    
    snakePosition = eval(str(snake.pos()))

    SnakePosition = screenTravel(snake,snakePosition)

    history.append(snakePosition)
    
    while len(history) > length:
        history.pop(0)
        snake.clearstamps(1)
    if len(set(history)) != len(history):
        gameOver()
        return()
    
    if foodLocation in history:
        length += 1
        foodLocation = (None, None)
        food.clearstamps(1)
        foodExists = False
        
    snake.stamp()
    if foodExists == False:
        foodSpawn()
    bg.ontimer(travel,300)

def main():
    
    onkeypress(lambda: None if snake.heading() == 270 else snake.seth(90), "Up")
    onkeypress(lambda: None if snake.heading() == 180 else snake.seth(0), "Right")
    onkeypress(lambda: None if snake.heading() == 0 else snake.seth(180), "Left")
    onkeypress(lambda: None if snake.heading() == 90 else snake.seth(270), "Down")

    bg.listen()
    travel()
    bg.mainloop()

if __name__ == "__main__":
    main()
