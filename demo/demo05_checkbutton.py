# -*- coding: utf-8 -*-
# @Time: 2019/8/4 20:44
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo05_checkbutton.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("checkbutton demo_1")
        self.root.geometry("500x470")

        # 默认未选中
        self.checkbutton1_var = IntVar()
        self.checkbutton1 = Checkbutton(self.root, text = "1 or 0", variable = self.checkbutton1_var, command = self.is_select_checkbutton1)
        self.checkbutton1.pack()

        # 默认选中
        self.checkbutton2_var = StringVar()
        self.checkbutton2 = Checkbutton(self.root, text = "男 or 女", variable = self.checkbutton2_var, command = self.is_select_checkbutton2, onvalue = "男", offvalue = "女")
        self.checkbutton2.deselect()
        # self.checkbutton2.select()
        self.checkbutton2.pack()

        # print(self.checkbutton1_var.get(), self.checkbutton2_var.get())

    def is_select_checkbutton1(self):
        # print(self.checkbutton1_var.get())
        if self.checkbutton1_var.get() == 1:
            print("选中")
        if self.checkbutton1_var.get() == 0:
            print("未选中")

    def is_select_checkbutton2(self):
        if self.checkbutton2_var.get() == "男":
            print("你选择的是男")
        if self.checkbutton2_var.get() == "女":
            print("你选择的是女")


if __name__ == '__main__':
    App().root.mainloop()
