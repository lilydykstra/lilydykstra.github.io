#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:32:51 2021

@author: sazamore

Math art

"""
import turtle, math

#equations from https://www.flerlagetwins.com/2017/11/beyond-me-part-3-parametric-equations_45.html?showComment=1562434668701&m=1
#  t : -8 to 8
# x = 6*SIN(13.58*[t])*ROUND(SQRT(COS(COS(7.4*[t]))),0)
# y = 6*POWER(COS(13.58*[t]),4)*SIN(SIN(7.4*[t]))
turtle.tracer(0)

# set up turtle
p = turtle.Turtle(visible=False) # this is not a descriptive name
s = p.getscreen() # this also is not a descriptive name
s.bgcolor("blue3")
p.color("cyan4")
p.pensize(6)
p.up()

# set up beginning of pattern
scale = 330 # make the pattern big enough to fill the screen
t = math.radians(-600)
x = math.sin(13.58*t) * round(math.sqrt(math.cos(math.cos(7.4*t))),0)
y = math.cos(13.58*t)**4 * math.sin(math.sin(7.4*t))

# go to start position
p.goto(x*scale,y*scale) 
p.down()

for t in range(-600,600):
    # iterate through values to draw parametric pattern
    t = math.radians(t)
    x = math.sin(13.58*t) * round(math.sqrt(math.cos(math.cos(7.4*t))),0)
    y = math.cos(13.58*t)**4 * math.sin(math.sin(7.4*t))
    p.goto(x*scale,y*scale)

# Clean up
p.up()
s.update()
turtle.done()