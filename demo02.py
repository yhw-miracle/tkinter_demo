# -*- coding: utf-8 -*-
# @Time: 2019/8/3 21:00
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo02.py
# @Software: PyCharm
from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master = master)
        frame.pack()

        self.button = Button(frame, text = "exit", fg = "#FF6A00", command = frame.quit)
        self.button.pack(side = RIGHT)

        self.hi_button = Button(frame, text = "hello", command = self.say_hi)
        self.hi_button.pack(side = LEFT)

    def say_hi(self):
        print("hello, world!")


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
