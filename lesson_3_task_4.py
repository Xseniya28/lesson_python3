from turtle import *

n = Turtle()
n.speed(0)
n.screen.setup(1200, 800)

#Настройки карандаша 
n.color("black")
n.pensize(3)

#Голова мышки
n.penup()
n.goto(0, -70)
n.pendown()
n.begin_fill()
n.fillcolor("gray")
n.circle(140)
n.end_fill()

#Левое ухо
n.up()
n.goto(-40, 195)
n.down()
n.begin_fill()
n.fillcolor("gray")
n.setheading(80)
n.circle(60, 270)
n.end_fill()

#Правое ухо
n.up()
n.goto(120, 135)
n.down()
n.begin_fill()
n.fillcolor("gray")
n.setheading(5)
n.circle(60, 270)
n.end_fill()

#Левый глаз 
n.penup()
n.goto(-80, 100)
n.pendown()
n.begin_fill()
n.fillcolor("white")
n.circle(25)
n.end_fill()

# Правый глаз
n.penup()
n.goto(50, 100)
n.pendown()
n.begin_fill()
n.fillcolor("white")
n.circle(25)
n.end_fill()

# Левая зрачок
n.penup()
n.goto(-60, 100)
n.pendown()
n.begin_fill()
n.fillcolor("black")
n.circle(10)
n.end_fill()

# Правая зрачок
n.penup()
n.goto(60, 100)
n.pendown()
n.begin_fill()
n.fillcolor("black")
n.circle(10)
n.end_fill()

# Нос
n.up()
n.goto(30, 35)
n.down()
n.begin_fill()
n.fillcolor("pink")
n.setheading(60)
n.circle(30, 240)
n.end_fill()

# Усы
n.up()
n.goto(10, 50)
n.down()
n.setheading(10)
n.forward(140)

n.up()
n.goto(10, 50)
n.down()
n.setheading(0)
n.forward(150)

n.up()
n.goto(10, 50)
n.down()
n.setheading(-10)
n.forward(140)

n.up()
n.goto(-10, 50)
n.down()
n.setheading(180)
n.forward(150)

n.up()
n.goto(-10, 50)
n.down()
n.setheading(170)
n.forward(140)

n.up()
n.goto(-10, 50)
n.down()
n.setheading(190)
n.forward(140)

# Рот
n.penup()
n.goto(-30, 0)
n.pendown()
n.color("black")
n.right(250)
n.circle(40, 120)

n.screen.exitonclick()
n.screen.mainloop()