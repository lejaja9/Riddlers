#Project Euler Question 85 https://projecteuler.net/problem=85

import turtle

def num_rec(m,n):
    num = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            rec = (m-i+1)*(n-j+1)
            num += rec
    return num


ans = [2000000,0,0]
m = 1
n = 1
gap = 2000000
while True:
    temp_gap = abs(2000000 - num_rec(m, n))
    if temp_gap < gap:
        gap = temp_gap
        n += 1
    else:
        if gap < ans[0]:
            ans = [gap, m, n-1]
            print(ans)
        if m > n:
            print(ans)
            break
        m += 1
        n = 1
        gap = 2000000


window = turtle.Screen()
turtle.hideturtle()
turtle.speed(9)
#square 1
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()
turtle.goto(-150,100)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor('gray')
turtle.left(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.goto(-200,150)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto(-200,250)
turtle.pendown()
turtle.pensize(3)
turtle.color('blue')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

#square 2
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
turtle.right(90)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()
turtle.goto(150,100)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor('gray')
turtle.left(90)
turtle.forward(150)
turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.goto(100,200)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.penup()
turtle.goto(100,150)
turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto(150,250)
turtle.pendown()
turtle.pensize(3)
turtle.color('blue')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

#square 3
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
turtle.right(90)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor('gray')
turtle.left(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.pensize(3)
turtle.color('blue')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

#square 4
turtle.penup()
turtle.goto(-200,-300)
turtle.pendown()
turtle.pensize(3)
turtle.color('black')
turtle.right(90)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()
turtle.goto(-150,-300)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor('gray')
turtle.left(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-100,-300)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.goto(-200,-250)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto(-200,-250)
turtle.pendown()
turtle.pensize(3)
turtle.color('blue')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

window.exitonclick()