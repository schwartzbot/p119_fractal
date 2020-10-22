import turtle as turtle

p = turtle.Turtle()
p.penup()
p.goto(0, -50)
p.setheading(0)

len = 50
def __branch__: 
    p.forward(len)
    p.setheading(-45)

wn = turtle.Screen()
wn.mainloop()