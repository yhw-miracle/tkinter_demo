# -*- coding: utf-8 -*-
# @Time: 2019/8/5 16:17
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo012_menubutton.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("menubutton demo")
        self.root.geometry("500x470")

        menubutton1 = Menubutton(self.root, text = "show menubutton", relief = RAISED)
        menu1 = Menu(menubutton1, tearoff = 0)
        menubutton1.config(menu = menu1)

        test1 = IntVar()
        test2 = IntVar()

        menu1.add_checkbutton(label = "test1", variable = test1)
        menu1.add_checkbutton(label = "test2", variable = test2)

        menubutton1.pack()


if __name__ == '__main__':
    App().root.mainloop()
