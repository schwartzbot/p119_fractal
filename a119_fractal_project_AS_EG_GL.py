from turtle import *
import turtle as turtle

p = turtle.Turtle()


p.speed('fastest') 

# turning the turtle to face upwards 
p.rt(-90) 

# the acute angle between 
# the base and branch of the Y 
angle = 30

# function to plot a Y 
def y(sz, level): 

	if level > 0: 
		colormode(255) 
		
		# splitting the rgb range for green 
		# into equal intervals for each level 
		# setting the colour according 
		# to the current level 
		p.pencolor(0, 255//level, 0) 
		
		# drawing the base 
		p.fd(sz) 

		p.rt(angle) 

		# recursive call for 
		# the right subtree 
		y(0.8 * sz, level-1) 
		
		p.pencolor(0, 255//level, 0) 
		
		p.lt( 2 * angle ) 

		# recursive call for 
		# the left subtree 
		y(0.8 * sz, level-1) 
		
		p.pencolor(0, 255//level, 0) 
		
		p.rt(angle) 
		p.fd(-sz) 
		
		
# tree of size 80 and level 7 
y(80, 7) 

wn = Screen()
wn.mainloop()
