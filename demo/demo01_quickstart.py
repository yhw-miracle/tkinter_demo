# -*- coding: utf-8 -*-
# @Time: 2019/8/3 20:52
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo01_quickstart.py
# @Software: PyCharm
from tkinter import *


if __name__ == '__main__':
    root = Tk()

    w = Label(root, text = "hello, world!")
    w.pack()

    root.mainloop()