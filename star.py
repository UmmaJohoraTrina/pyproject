
import turtle
 
trina_turtle = turtle.Turtle()
 
# first triangle for star
trina_turtle.forward(100) # draw base
 
trina_turtle.left(120)
trina_turtle.forward(100)
 
trina_turtle.left(120)
trina_turtle.forward(100)
 
trina_turtle.penup()
trina_turtle.right(150)
trina_turtle.forward(50)
 
# second triangle for star
trina_turtle.pendown()
trina_turtle.right(90)
trina_turtle.forward(100)
trina_turtle.right(120)
trina_turtle.forward(100)
 
trina_turtle.right(120)
trina_turtle.forward(100)
 
turtle.done()
