# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:06
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo06_entry.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("entry demo")
        self.root.geometry("500x470")

        self.entry1 = Entry(self.root)
        self.entry1.pack()

        self.entry1.delete(0, END)
        self.entry1.insert(0, "hello, world!")

        self.frame_username = Frame(self.root)
        self.frame_username.pack()
        self.username = self.make_entry(self.frame_username, "username", 10)

        self.frame_password = Frame(self.root)
        self.frame_password.pack()
        self.password = self.make_entry(self.frame_password, "password", 10, show = "*")

    def make_entry(self, parent, caption, width = None, **option):
        Label(parent, text = caption).pack(side =LEFT)
        entry = Entry(parent, **option)

        if width:
            entry.config(width = width)

        entry.pack(side = RIGHT)
        return entry


if __name__ == '__main__':
    App().root.mainloop()
