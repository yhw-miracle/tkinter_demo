# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:18
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo07_frame.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("frame demo")
        self.root.geometry("500x470")

        self.frame = Frame(master = self.root, width = 200, height = 100, bg = "#FF6A00", relief = SUNKEN, bd = 5)
        self.frame.config(highlightbackground = "#123456", takefocus = False)
        self.frame.pack()


if __name__ == '__main__':
    App().root.mainloop()
