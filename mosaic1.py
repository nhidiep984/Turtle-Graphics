import turtle
import math

'''Move Pen'''
def move_pen(mosaic, location):
    mosaic.penup()
    mosaic.goto(location)
    mosaic.pendown()

'''Draw a circle'''
def draw_circle(mosaic, radius, tilt_angle):
    mosaic.circle(radius)
    mosaic.tilt(tilt_angle)

'''Draw a star'''
def draw_star(mosaic, distance, angle):
    for i in range(40):
        mosaic.forward(distance)
        mosaic.left(angle)

'''Draw the mosaic'''
def draw_mosaic(mosaic):
    mosaic.getscreen().bgcolor('black')
    mosaic.pencolor('#b1cbbb')
    mosaic.speed(10)
    draw_star(mosaic, 300, 170)
    move_pen(mosaic,(20,-140))
    draw_circle(mosaic, 200, 300)

def main():
    turtle.setup()
    mosaic = turtle.Turtle()
    draw_mosaic(mosaic)
    turtle.done()

main()
