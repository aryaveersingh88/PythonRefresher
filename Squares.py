# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:28:43 2018

@author: asingh368
"""

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
   
def draw_art():
    
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle to draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    window.exitonclick()
    
draw_art()