'''
get a hirst img and save 
import colorgram

rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

pip install colorgram

then create a series of 'dots' size 20 in the selected colors
10 x 10
'''

import colorgram
import turtle
import random

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.jpg', 10)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
rgb_colors = []
for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	rgb_colors.append((r,g,b))

turtle_module.colormore(255)
t = turtle_module.Turtle()
t.penup()
t.speed(fastest)
t.hideturtle()
t.setheading(225)
t.forward(250)
t.setheading(0)

for count in range 101:
		t.dot(20, random.choice(rgb_colors))
		t.forward(50)
		if count %10 ==0:
			t.setheading(90)
			t.forward(50)
			t.setheading(180)
			t.forward(500)
			t.setheading(0)


		
