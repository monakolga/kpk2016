# coding=utf-8
from turtle import Turtle
t=Turtle()
t.penup()

def test_drawman():
    """
    Тестирование работы Чертежника
    :return: None
    """

    pen_down()
    for i in range(5):
        on_vector(1,2)
        on_vector(0.-2)
    pen_up()
    to_point(0,0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(x,y):
    pass

def to_point(x,y):
    pass

if __name__=='__mail__':
    test_drawman()