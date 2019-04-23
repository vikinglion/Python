#!/usr/bin/env python
# coding=UTF-8

stulist = [
{'name':'wu xiaohai','age':'20','class':'201'},
{'name':'tong nihan','age':'20','class':'198'}
] 
num = 0

def add_info():
	stu = {}
	stu['name'] = input("请输入名字:\n")
	stu['age'] = input("请输入年龄:\n")
	stu['class'] = input("请输入班级:\n")
	stulist.append(stu)
		
def showStu(stulist):
	if len(stulist) == 0:
		print("没有学员信息可以输出")
		return
	else:
		print("|{0:<5}|{1:<10}|{2:<5}|{3:<5}|".format("id","name","age","class"))
		print("-"*38)
		for i in range(len(stulist)):
			print("|{0:<5}|{1:<10}|{2:<5}|{3:<5}|".format(i+1,stulist[i]['name'],stulist[i]['age'],stulist[i]['class']))

while True:
	print("="*12,"学员管理系统","="*12)
	print("{0:1}{1:13}{2:15}".format(" ","1.查看学员信息","2.添加学员信息")) 
	print("{0:1}{1:13}{2:15}".format(" ","3.删除学员信息","4.quit"))
	print("="*38)

	key = input("请输入对应的选择：\n")


	if key == "1":
		print("="*12,"学员信息浏览","="*12)
		showStu(stulist)
		
	elif key == "2":
		print("="*12,"学员信息添加","="*12)
		add_info()
		
	elif key == "3": 
		print("="*12,"学员信息删除","="*12)
		i = input("请选择要删除的学员信息编号:\n")
		if int(i) not in range(len(stulist)):
			print("没有该编号可删除")
			continue
		else:	
			del stulist[int(i)-1]
		
	elif key == "4":
		print("再见")
		break
		
	else:
		print("请输入有效数字！")
	input("按回车继续")
