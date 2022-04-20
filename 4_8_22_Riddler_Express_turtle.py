import turtle

window = turtle.Screen()
#turtle.hideturtle()
turtle.speed(9)
#square 1
turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
turtle.fillcolor('red')
turtle.begin_fill()

for i in range(4):
    turtle.forward(200)
    turtle.left(90)

turtle.end_fill()

#square 2
turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
turtle.goto(-50, 175)
turtle.forward(175)
turtle.goto(50, 100)


window.exitonclick()