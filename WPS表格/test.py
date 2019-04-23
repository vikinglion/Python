#!usr/bin/env python
#coding=utf-8

import xlrd

dirname = "波特图数据.xlsx"

def read_excel():
#打开文件
	workbook = xlrd.open_workbook(rf'F:\Program Files\Geany\WPS表格\{dirname}')
	print(workbook.sheet_names())
	sheet1 = workbook.sheet_by_name('Sheet1')
	#获取行内容
	print(sheet1.row_values(2))
	#获取列内容
	print(sheet1.col_values(3))
	#获取单元格内容
	print(sheet1.cell_value(0,0))
	print("\n"*3)
	for i in range(sheet1.nrows):
		print(sheet1.row_values(i))

if __name__ == '__main__':
	read_excel()
