#!/usr/bin/env python
# -*- coding=utf-8 -*- 
SYMBOLS = {')': '(',}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()
def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            print(arr)
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False
    if len(arr) != 0:return False
    else:return True
		


print(check("(dfsadf)()"))
print(check("(()"))
print(check("fnva(mfd)gfv(yncxw()lcmx)lwql((i))"))
print(check("())"))
