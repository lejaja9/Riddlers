import turtle

window = turtle.Screen()
turtle.hideturtle()
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

#square three
turtle.penup()
turtle.goto(125, 175)
turtle.pendown()
turtle.right(90)
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(175)
turtle.goto(50, -100)
turtle.goto(50, 100)
turtle.goto(125, 175)
turtle.end_fill()

#grid
turtle.penup()
turtle.left(90)
turtle.goto(-150, -33)
turtle.pendown()
turtle.pensize(1)
turtle.forward(200)
turtle.goto(125, 58)

turtle.penup()
turtle.goto(-150, 33)
turtle.pendown()
turtle.pensize(1)
turtle.forward(200)
turtle.goto(125, 116)

turtle.penup()
turtle.goto(-84, 100)
turtle.right(90)
turtle.pendown()
turtle.pensize(1)
turtle.forward(200)

turtle.penup()
turtle.goto(-18, 100)
turtle.pendown()
turtle.pensize(1)
turtle.forward(200)

turtle.penup()
turtle.goto(-84, 100)
turtle.pendown()
turtle.pensize(1)
turtle.goto(8, 175)

turtle.penup()
turtle.goto(-18, 100)
turtle.pendown()
turtle.pensize(1)
turtle.goto(67, 175)

turtle.penup()
turtle.left(90)
turtle.goto(-117, 125)
turtle.pendown()
turtle.pensize(1)
turtle.forward(192)
turtle.goto(75, -67)

turtle.penup()
turtle.goto(-84, 150)
turtle.pendown()
turtle.pensize(1)
turtle.forward(184)
turtle.goto(100, -33)


window.exitonclick()