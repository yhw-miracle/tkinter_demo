# -*- coding: utf-8 -*-
# @Time: 2019/8/4 21:51
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo11_menu.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("menu demo")
        self.root.geometry("500x470")

        self.menubar = Menu(self.root)

        self.file_menu = Menu(self.menubar, tearoff = 0)
        self.file_menu.add_command(label = "Open", underline = 0, command = lambda : print("open..."))
        self.file_menu.add_command(label = "Save", underline = 0, command = lambda : print("save..."))
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", underline = 0,  command = lambda : print("exit"))
        # self.file_menu.add_command(label = "Exit", underline = 0, command = sys.exit())   # ---> The code is unreached
        self.menubar.add_cascade(label = "File", menu = self.file_menu)

        self.edit_menu = Menu(self.menubar, tearoff = 0)
        self.edit_menu.add_command(label = "Cut", underline = 0, command = lambda : print("cut..."))
        self.edit_menu.add_command(label = "Copy", underline = 0, command = lambda : print("copy..."))
        self.edit_menu.add_command(label = "Paste", underline = 0, command = lambda : print("paste..."))
        self.edit_menu.add_command(label = "edit", underline = 0, command = lambda : print("edit..."))
        self.menubar.add_cascade(label = "Edit", menu = self.edit_menu)

        self.help_menu = Menu(self.menubar, tearoff = 0)
        self.help_menu.add_command(label = "About", underline = 0, command = lambda : print("about"))
        self.menubar.add_cascade(label = "Help", menu = self.help_menu)

        self.root.config(menu = self.menubar)


if __name__ == '__main__':
    App().root.mainloop()