#Oct 25 Riddle and Viz: "If a stick of length x is broken into three pieces, what is the probability that the three pieces can be used to construct a triangle?"
import scipy.integrate as integrate
import turtle

def f(x):
    return x

ans = integrate.quad(f, 0, 0.5)
print(ans[0]*2)


window = turtle.Screen()
# turtle.hideturtle()
# turtle.color('DarkGray')
# turtle.pensize(19)
# turtle.speed(1)
# turtle.penup()
# turtle.forward(-100)
# turtle.pendown()
# turtle.forward(200)
# turtle.penup()
# turtle.home()
# turtle.sety(20)
# turtle.left(-90)
# turtle.pensize(3)
# turtle.color('black')
# turtle.pendown()
# turtle.forward(40)
# window.exitonclick()

turtle.hideturtle()
turtle.pensize(19)
turtle.penup()
turtle.forward(-100)
turtle.pendown()
turtle.color('DarkGray')
turtle.forward(100)
# turtle.forward(-200)
# turtle.dot(9, 'black')
# window.exitonclick()

# turtle.color('Yellow')
# turtle.shape("square")
# turtle.shapesize(0.9, 1.0, 1)
# for count in range(50):
#     turtle.stamp()
#     turtle.forward(1)
# #turtle.forward(50)
# turtle.color('DarkGray')
# for count in range(9):
#     turtle.stamp()
#     turtle.forward(1)
# turtle.forward(41)
# turtle.penup()
# turtle.forward(-150)
# turtle.dot(9, 'black')
# window.exitonclick()

turtle.color('Yellow')
turtle.shape("square")
turtle.shapesize(0.9, 1, 1)
for count in range(75):
    turtle.stamp()
    turtle.forward(1)
#turtle.forward(50)
turtle.color('DarkGray')
for count in range(9):
    turtle.stamp()
    turtle.forward(1)
turtle.forward(16)
turtle.penup()
turtle.forward(-125)
turtle.dot(9, 'black')
window.exitonclick()


