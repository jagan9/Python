import turtle

pac=turtle.Screen()
pac.bgcolor("light green")
pac.title("Jagan")

star = turtle.Turtle()

star.color("red","yellow")

star.begin_fill()
for i in range(10):
    star.forward(100)
    if(i%2==0):
    	star.right(140)
    else:
	    star.left(68)
star.setx(-100)
star.fd(100)
star.end_fill()
turtle.done()