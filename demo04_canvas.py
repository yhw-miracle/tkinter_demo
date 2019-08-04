# -*- coding: utf-8 -*-
# @Time: 2019/8/4 20:34
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo04_canvas.py
# @Software: PyCharm
from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("canvas demo")
        self.root.geometry("500x470")

        self.canvas_demo = Canvas(self.root, width = 200, height = 100)
        self.canvas_demo.pack()

        self.canvas_demo.create_line(0, 0, 200, 100)
        self.canvas_demo.create_line(0, 100, 200, 0, fill = "red", dash = (4, 4))

        self.canvas_demo.create_rectangle(50, 25, 150, 75, fill = "green")


if __name__ == '__main__':
    App().root.mainloop()

