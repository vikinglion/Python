#!/usr/bin/env python
#coding=utf-8

import itchat
import os
import time
import cv2
from PIL import ImageGrab

sendMsg = u"{消息助手}:暂时无法回复"
usageMsg = u"使用方法:\n1.运行CMD命令: cmd xxx \n"\
u"2.关机\n"u"3.获取当前电脑用户: cap \n4.截屏\n5.启用消息助手: 启用\n"\
u"6.关闭消息助手: 关闭\n"u"7.切换手机用户:切换\n"u"9.登出"

flag = 0
nowTime = time.localtime()
filename = str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".txt"
myfile = open(filename, 'w')

@itchat.msg_register('Text')
def text_reply(msg):
	global flag
	message = msg['Text']
	fromName = msg['FromUserName']
	toName = msg['ToUserName']
	
	if toName == "filehelper":
		if message == "cap":
			cap = cv2.VideoCapture(0)
			ret, frame = cap.read()
			cv2.imwrite("wiexinTemp.jpg", frame)
			itchat.send("Capturing", 'filehelper')
			itchat.send_image("wiexinTemp.jpg", 'filehelper')
			itchat.send("Finished", 'filehelper')
			cap.release()
		if message == "截屏":
			im = ImageGrab.grab(0)
			im.save("screencapture.jpg")
			itchat.send_image("screencapture.jpg", 'filehelper')
		if message[0:3] == "cmd":
			os.system(message.strip(message[0:4]))
		if message == "关机":
			os.system("shutdown -s -t 0")
		if message == "启用":
			flag = 1
			itchat.send("消息助手已开启", "filehelper")
		if message == "关闭":
			flag = 0
			itchat.send("消息助手已关闭", "filehelper")
		if message == "切换":
			itchat.logout()
			itchat.auto_login()
		if message == "登出":
			itchat.logout()

	elif flag == 1:
		itchat.send(sendMsg, fromName)
		myfile.write(message)
		myfile.write("\n")
		myfile.flush()
		
if __name__ == '__main__':
	itchat.auto_login(hotReload = True)
	itchat.send(usageMsg, "filehelper")
	itchat.run()
	
