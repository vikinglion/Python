#!/usr/bin/env python

import tkinter as tk

top = tk.Tk()
quit = tk.Button(top, text = 'Hello world!', command = top.quit)
quit.pack()
tk.mainloop()
