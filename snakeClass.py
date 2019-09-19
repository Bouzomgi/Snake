from turtle import *
import random


class Game:
    #Initializes our Turtle that will create our snake, and another Turtle as our food blocks
    def __init__(self):
        self.bg = Screen()
        self.bg.screensize(300,300)
        self.snake = Turtle()
        self.snake.penup()
        self.snake.speed(0)
        self.snake.shape("square")

        self.food = Turtle()
        self.food.hideturtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.color("red")

        self.firstFoodSpawn = False
        self.length = 3
        self.history = []
        self.foodLocation = (None, None)

    #Eliminates each segment of the snake backwards and prints out a message stating the user has lost
    def gameOver(self):
        self.food.clearstamps(1)
        self.snake.clearstamps(1)
        self.history.pop()    
        if self.history:
            self.bg.ontimer(self.gameOver, 300)
        else:
            self.bg.delay(25)
            self.snake.hideturtle()
            self.food.goto(140, 190)
            self.food.color("red")
            self.food.write("You Lose", False, align = "center", font=("Comic Sans", 50, "bold"))

    #If the snake hits a wall, screenTravel teleports the snake to the opposite wall
    def screenTravel(self,position):
        if position[0] > 300:
            position = (-300 , position[1])
            self.snake.goto(position[0], position[1])

        if position[0] < -300:
            position = (300 , position[1])
            self.snake.goto(position[0], position[1])

        if position[1] > 240:
            position = (position[0], -240)
            self.snake.goto(position[0], position[1])

        if position[1] < -240:
            position = (position[0], 240)
            self.snake.goto(position[0], position[1])

        return(position)

    #Spawns a piece of food in a random place on the board as long as that place isn't where the Snake currently is.
    def foodSpawn(self):
        randX, randY = 30 * random.randint(-9,9), 30 * random.randint(-8,8)
        while (randX, randY) in self.history:
            randX, randY = 30 * random.randint(-9,9), 30 * random.randint(-8,8)
            
        self.food.setpos(randX, randY)
        self.food.stamp()
        self.foodLocation = eval(str(self.food.pos()))

    #Here the snake moves forward, and we reassign the values of our list stating where each segment of the Snake is located. We eliminate 
    #any old snake stamps to ensure the Snake is the proper length. We also check if the Snake is on top of the food, and if it is, we add one to 
    #the length and spawn another food
    def travel(self):
        self.snake.forward(30)
        snakePosition = eval(str(self.snake.pos()))
        snakePosition = self.screenTravel(snakePosition)
        self.history.append(snakePosition)
        
        while len(self.history) > self.length:
            self.history.pop(0)
            self.snake.clearstamps(1)
        if len(set(self.history)) != len(self.history):
            self.gameOver()
            return()
        
        if self.foodLocation in self.history:
            self.length += 1
            self.foodLocation = (None, None)
            self.food.clearstamps(1)
            self.foodSpawn()
            
        self.snake.stamp()

        if self.firstFoodSpawn == False:
            self.foodSpawn()
            self.firstFoodSpawn = True
            
        self.bg.ontimer(self.travel,300)

    #Here we continuously check for keyboard inputs and connect our Snake's movements to them. 
    def main(self):
        
        onkeypress(lambda: None if self.snake.heading() == 270 else self.snake.seth(90), "Up")
        onkeypress(lambda: None if self.snake.heading() == 180 else self.snake.seth(0), "Right")
        onkeypress(lambda: None if self.snake.heading() == 0 else self.snake.seth(180), "Left")
        onkeypress(lambda: None if self.snake.heading() == 90 else self.snake.seth(270), "Down")

        self.bg.listen()
        self.travel()
        self.bg.mainloop()

if __name__ == "__main__":
    SnakeGame = Game()
    SnakeGame.main()


    
