# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:40
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo10_listbox.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("listbox demo")
        self.root.geometry("500x470")

        # self.listbox = Listbox(self.root, selectmode = EXCEPTION)
        self.listbox = Listbox(self.root, selectmode = SINGLE)

        for i in range(10):
            self.listbox.insert(END, i)
        self.listbox.pack()

        self.button1 = Button(self.root, text = "delete", command = lambda listbox = self.listbox : listbox.delete(ANCHOR))
        self.button1.pack()


if __name__ == '__main__':
    App().root.mainloop()