import turtle

rec = turtle.Turtle()
rec.speed(7)
down = turtle.Turtle()
down.speed(7)
chakra = turtle.Turtle()
chakra.speed(10)

chakra2 = turtle.Turtle()
chakra2.speed(10)

gola = turtle.Turtle()
gola.speed(10)

gola2 = turtle.Turtle()
gola2.speed(10)



rec.fillcolor("orange")
rec.color("orange")
rec.penup()
rec.left(90)
rec.forward(320)
rec.left(90)
rec.forward(600)
rec.pendown()
rec.begin_fill()
rec.backward(1200)
rec.left(90)
rec.forward(180)
rec.left(90)
rec.backward(1200)
rec.left(90)
rec.end_fill()




down.fillcolor("green")
down.penup()
down.right(90)
down.forward(320)
down.right(90)
down.forward(600)
down.pendown()
down.begin_fill()
down.backward(1200)
down.right(90)
down.forward(180)
down.right(90)
down.backward(1200)
down.right(90)
down.end_fill()

gola.penup()
gola.backward(4)
gola.right(90)
gola.forward(120) # kam karne pe upar jata hia
gola.left(90)
gola.pendown()
gola.fillcolor("blue")
gola.begin_fill()
gola.circle(120)
gola.end_fill()



gola2.penup()
gola2.backward(4)
gola2.right(90)
gola2.forward(116) # kam karne pe upar jata hia
gola2.left(90)
gola2.pendown()
gola2.fillcolor("white")
gola2.begin_fill()
gola2.circle(115)
gola2.end_fill()






chakra.penup()
chakra.forward(105)
chakra.right(90)
chakra.forward(15)
chakra.left(90)
chakra.pendown()
chakra.fillcolor("blue")
chakra.begin_fill()
for i in range(24):
    chakra.color("blue")
    chakra.left(165)
    chakra.forward(220 - (i))
chakra.end_fill()

chakra2.penup()
chakra2.forward(105)
chakra2.right(90)
chakra2.forward(15)
chakra2.left(90)
chakra2.pendown()
for i in range(24):
    chakra2.color("white")
    chakra2.left(165)
    chakra2.forward(220 - i/2)







turtle.done()
