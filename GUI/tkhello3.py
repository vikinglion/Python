#!/usr/bin/env python
#coding=utf-8

from sound_track import *

import tkinter as tk


top = tk.Tk()
top.geometry('250x150')

hello = tk.Label(top, text = 'Hello world!')
hello.pack()



quit = tk.Button(top, text = 'Quit', command = top.quit, bg = 'red', fg = 'white')
quit.pack(fill = tk.X, expand = 1)

b1 = tk.Button(top, text = "Assassin's Creed 3", command = sound_track1, bg = 'white', fg = "yellow")
b1.pack(fill = tk.X, expand = 1)

b2 = tk.Button(top, text = 'Heart of Iron4', command = sound_track2, bg = 'white', fg = "green")
b2.pack(fill = tk.X, expand = 1)

b3 = tk.Button(top, text = 'Fallout4', command = sound_track3, bg = 'white', fg = "blue")
b3.pack(fill = tk.X, expand = 1)

tk.mainloop()
