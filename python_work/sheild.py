#!usr/bin/env python
#coding=utf-8

import turtle as t

def setpen(x,y):
	#̧��
	t.penup()
	#�ƶ����ʵ�(x,y)
	t.goto(x,y)
	#���
	t.pendown()
	t.setheading(0)
	
def circle(x, y, r, color):
	n = 36
	angle = 360 / n
	pi = 3.1415926
	#�ܳ�
	c = 2 * pi * r
	#ÿ���ߵĳ���
	l = c / n
	#��ʼλ��
	start_x = x - l / 2
	start_y = y + r
	#�ƶ�����
	setpen(start_x, start_y)
	#ѡ�񻭱���ɫ
	t.pencolor(color)
	#ѡ�񱳾�ͼ
	t.fillcolor(color)
	#���
	t.begin_fill()
	for i in range(n):
		t.forward(l)
		t.right(angle)
	t.end_fill()
	
def five_star(l):
	setpen(0, 0)
	t.setheading(162)
	t.forward(150)
	t.setheading(0)
	t.fillcolor('WhiteSmoke')
	t.begin_fill()
	t.hideturtle()
	t.penup()
	for i in range(5):
		t.forward(l)
		t.right(144)
	t.end_fill()
	
def sheild():
	circle(0, 0, 300, 'red')
	circle(0, 0, 250, 'white')
	circle(0, 0, 200, 'red')
	circle(0, 0, 150, 'blue')
	five_star(284)
	
if __name__ == '__main__':
	sheild()
	#���������ͼ
	t.done()
