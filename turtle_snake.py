
from turtle import Turtle 
import random

# initial screen setup
screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black")
screen.title("snake")

# create 3 squares
turtle.colormode(255)# range of colors
my_turtle =Turtle()

my_turtle.pensize(15)
my_turtle.speed("fastest")
my_turtle.pencolor(r,g,b)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return(r,g,b)
	
	
	
for _ in range(200):
	my_turtle.color(random_color())
	my_turtle.fwd(10)
	my_turtle.rt(90)
	
	
	
	
	
	
screen.exitonclick()





