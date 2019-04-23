#!usr/bin/env python
#coding=utf-8

import turtle as t
def setpen(x, y):
	#抬笔
	t.penup()
	#移动画笔到(x,y)
	t.goto(x,y)
	#落笔
	t.pendown()
	t.setheading(0)
	
def half_h1(start_x, start_y, color):
	angle1 = 4
	angle2 = 2
	n = 56
	m = 23
	setpen(start_x, start_y)
	t.left(70)
	t.fillcolor('pink')
	t.begin_fill()
	for i in range(n):
		t.pencolor(color)
		t.forward(10)
		t.right(angle1)
	t.forward(60)
	for i in range(m):
		t.pencolor(color)
		t.forward(10)
		t.left(angle2)
	t.end_fill()

def half_h2(start_x, start_y, color):
	angle1 = 4
	angle2 = 2
	n = 56
	m = 23
	setpen(start_x, start_y)
	t.left(110)
	t.fillcolor('pink')
	t.begin_fill()
	for i in range(n):
		t.pencolor(color)
		t.forward(10)
		t.left(angle1)
	t.forward(60)
	for i in range(m):
		t.pencolor(color)
		t.forward(10)
		t.right(angle2)	
	t.end_fill()

def word():
	t.hideturtle()
	setpen(-160, 60)
	t.write("姝姝爱你哟！！！", font=("微软雅黑", 40, "normal"))
	setpen(-100, -30)
	t.write("(^3^)", font=("Arial", 60, "bold"))
	
if __name__ == '__main__':
	half_h1(0, 150, 'red')
	setpen(0, 150)
	half_h2(0, 150, 'red')
	word()
	t.done()
