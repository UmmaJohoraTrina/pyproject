import turtle

trina_turtle=turtle.Turtle()
trina_turtle.speed(15)
def triangle():

 trina_turtle.forward(100)
 trina_turtle.right(120)
 trina_turtle.forward(100)
 trina_turtle.right(120)
 trina_turtle.forward(100)
 
for i in range(3):
 triangle()
trina_turtle.right(90)
trina_turtle.forward(200)
