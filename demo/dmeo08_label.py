# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:27
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: dmeo08_label.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("label demo_1")
        self.root.geometry("500x470")

        self.label = Label(self.root, text = "demo_1", anchor = W, bg = "#FF6A00", bd = 5)
        self.label.config(cursor = "gumby", fg = "#987645")
        self.label.config(font = ("time", 14, "bold"))
        self.label.config(state = NORMAL, takefocus = True)
        self.label.config(underline = 0)
        self.label.pack()


if __name__ == '__main__':
    App().root.mainloop()
