# -----------------------------------------------------------
# Tvoreni grafu
# Vytvoril Matej Matejka
# -----------------------------------------------------------
import turtle

# Jednotlivé hodnoty
vstup = open("nahodna_cisla.txt", "r")
nm = str(vstup.readline())
xln = int(vstup.readline())
xpt = int(vstup.readline())
yln = int(vstup.readline())
cur = int(vstup.readline())

# Okno
sc = turtle.Screen()
turtle.title(nm)
sc.setup(800, 800)


# Turtle parametry
t = turtle.Turtle()
t.speed('fastest')
t.ht()
turtle.tracer(0, 0)


# Nazev grafu
def title():
    t.penup()
    t.setpos(-125, 300)
    t.write(nm, font=("Arial", 20, "normal", ))

# Osa x
def xline():
    t.setpos(-150, -150)
    t.pendown()
    t.forward(25 * xln)
    t.penup()
    t.setpos(-150, -150)

# Body na ose x
def xpoint():
    xptnum = 1
    for x in range(xpt):
        t.forward(25 * xln / xpt)
        t.pendown()
        t.dot()
        t.penup()
        t.right(90)
        t.forward(25)
        t.write(xptnum, font=("Arial", 10, "normal", ))
        t.left(180)
        t.forward(25)
        t.right(90)
        xptnum = xptnum + 1


# Osa y
def yline():
    t.setpos(-150, -150)
    t.pendown()
    t.left(90)
    t.forward(5 * yln)
    t.penup()

# Krivka
def curve():
    t.setpos(-150, -150)
    curcol = vstup.readline()
    t.pencolor(curcol.strip())
    curnumval = int(vstup.readline())
    curvalin = vstup.readline()
    curval = curvalin.split(" ")
    for i in range(curnumval):
        t.pendown()
        cur = int(curval[0])
        t.setpos(t.xcor() + 25 * xln / xpt, -150 + 5 * cur)
        del curval[0]
    t.penup()
def curves():
    for c in range(cur):
        curve()
    
# Volani jednotlivych funkci
title()
xline()
xpoint()
yline()
curves()
turtle.update()
turtle.exitonclick()

