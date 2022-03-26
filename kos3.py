from turtle import *
import turtle
import time

tur = turtle.Turtle()
tur_txt = turtle.Turtle()
tur_txt.goto(tur.position()[0], tur.position()[1])
tur_txt.write("Python Guides")
time.sleep(2)
turtle.done()