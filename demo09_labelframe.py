# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:35
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo09_labelframe.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("labelframe demo")
        self.root.geometry("500x470")

        self.group = LabelFrame(self.root, text = "group", padx = 5, pady = 5)
        self.group.config(bd = 5)
        self.group.pack(padx = 10, pady = 10)

        self.entry = Entry(self.group)
        self.entry.pack()
        self.button = Button(self.group, text = "OK")
        self.button.pack()


if __name__ == '__main__':
    App().root.mainloop()