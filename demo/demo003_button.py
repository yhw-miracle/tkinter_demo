# -*- coding: utf-8 -*-
# @Time: 2019/8/4 19:49
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo03_button.py
# @Software: PyCharm
from tkinter import *

"""
Buttons can contain text or images.
"""


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("button demo_1")
        self.root.geometry("500x470")

        self.frame = Frame(master = self.root)
        self.frame.pack()

        self.button1 = Button(self.frame, text = "click button1", command = self.callback)
        self.button1.pack()

        self.button2 = Button(self.frame, text = "disabled", state = DISABLED)
        self.button2.pack()

        self.button3 = Button(self.frame, text = "specify size", command = self.callback(), padx = 10, pady = 10, relief = SUNKEN)
        self.button3.pack()

        self.button4 = Button(self.frame, text = "config")
        self.button4.config(activebackground = "#FF6A00", activeforeground = "#000010")

        self.button4.config(background = "#FFFAA0")
        self.button4.config(bg = "#FFFAA0", fg = "#999876")

        self.button4.config(borderwidth = 1)

        self.button4.config(compound = CENTER)

        self.button4.config(cursor = "gumby")

        self.button4.config(relief = SUNKEN)
        # self.button4.config(relief = RAISED)
        # self.button4.config(relief = GROOVE)
        # self.button4.config(relief = RIDGE)
        # self.button4.config(relief = FLAT)

        self.button4.config(state = ACTIVE)
        # self.button4.config(state = NORMAL)
        # self.button4.config(state = DISABLED)

        self.button4.config(underline = 1)
        self.button4.pack()

    def callback(self):
        print("click button1...")


if __name__ == '__main__':
    App().root.mainloop()
