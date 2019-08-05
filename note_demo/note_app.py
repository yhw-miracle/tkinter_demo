# -*- coding: utf-8 -*-
# @Time: 2019/8/5 12:31
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: note_app.py
# @Software: PyCharm
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class NoteApp(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500+200+100")
        self.root.title("Note")

        # 当前文件
        self.file_name = None
        # 当前文本区域内容
        self.textarea = None

        # 菜单
        self.root.config(menu = self.__init_menu())

        # 工具栏
        self.__init_toolbar()

        # 文本区域
        self.__init_textarea()

        # 状态栏
        self.__init_statusbar()

    def __init_menu(self):
        """
        初始化菜单
        :return: menubar
        """
        # 菜单栏
        menubar = Menu(self.root)

        # 文件子菜单
        file_menu = Menu(menubar, tearoff = 0)   # 去除菜单顶部分隔线
        file_menu.add_command(label = "新建", command = self.new_file)
        file_menu.add_command(label = "打开", command = self.open_file)
        file_menu.add_command(label = "保存", command = self.save_file)
        file_menu.add_command(label = "另存为", command = self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label = "退出", command = lambda : print('退出'))
        menubar.add_cascade(label = "文件", menu = file_menu)

        # 编辑子菜单
        edit_menu = Menu(menubar, tearoff = 0)
        edit_menu.add_command(label = "撤销", command = self.undo)
        edit_menu.add_command(label = "反撤销", command = self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label = "复制", command = self.copy)
        edit_menu.add_command(label = "剪切", command = self.cut)
        edit_menu.add_command(label = "粘贴", command = self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label = "全选", command = lambda : print("全选..."))
        edit_menu.add_command(label = "查找", command = lambda : print("查找..."))
        edit_menu.add_command(label = "替换", command = lambda : print("替换..."))
        edit_menu.add_separator()
        # 编辑 ---> 添加子菜单
        edit_menu_add = Menu(edit_menu, tearoff = 0)
        edit_menu_add.add_command(label = "添加时间", command = lambda : print("添加时间..."))
        edit_menu_add.add_command(label = "添加日期", command = lambda : print("添加日期..."))
        edit_menu_add.add_command(label = "添加作者", command = lambda : print("添加作者..."))
        edit_menu.add_cascade(label = "添加", menu = edit_menu_add)
        menubar.add_cascade(label = "编辑", menu = edit_menu)

        # 帮助子菜单
        help_menu = Menu(menubar, tearoff = 0)
        help_menu.add_command(label = "查看帮助", command = lambda : print("https://github.com/yhw-miracle"))
        help_menu.add_separator()
        help_menu.add_command(label = "关于", command = lambda : print("作者信息，隐私信息等"))
        menubar.add_cascade(label = "帮助", menu = help_menu)

        return menubar

    def __init_toolbar(self):
        """
        初始化工具栏
        :return:
        """
        toolbar_frame = Frame(self.root, height = 50)
        toolbar_frame.config(bg = "#FF6A00")
        toolbar_frame.pack(side = TOP, fill = X)

        new_file_button = Button(toolbar_frame, text = "新建", command = self.new_file)
        new_file_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        open_file_button = Button(toolbar_frame, text = "打开", command = self.open_file)
        open_file_button.grid(row = 0, column = 1, padx = 5, pady = 5)
        save_file_button = Button(toolbar_frame, text = "保存", command = self.save_file)
        save_file_button.grid(row = 0, column = 2, padx = 5, pady = 5)

    def __init_textarea(self):
        """
        初始化文本编辑区域
        :return:
        """
        textarea_frame = Frame(self.root)
        textarea_frame.pack(fill = BOTH, expand = YES)

        # 行号区域
        # line_num_label = Label(textarea_frame, width = 5, bg = "#FFFFF1")
        # line_num_label.pack(side = LEFT, fill = Y)
        line_num = Listbox(textarea_frame)
        line_num.config(bg = "#FFFFF1", width = 5)
        line_num.pack(side = LEFT, fill = Y)

        # 文本展示区域
        self.textarea = Text(textarea_frame, undo = True)
        self.textarea.config(bg = "#FFFFF0")
        self.textarea.pack(expand = YES, fill = BOTH)

        # 滚动条
        text_scroll = Scrollbar(self.textarea)
        self.textarea.config(yscrollcommand = text_scroll.set)
        text_scroll.config(command = self.textarea.yview)
        text_scroll.pack(side = RIGHT, fill = Y)

    def __init_statusbar(self):
        """
        初始化状态栏
        :return:
        """
        statusbar_frame = Frame(self.root, height = 50)
        statusbar_frame.config(bg = "#FF6A00")
        statusbar_frame.pack(side = BOTTOM, fill = X, expand = NO)

        line_label = Label(statusbar_frame, text = "第 1 行", bg = "#FF6A00")
        line_label.pack(side = RIGHT)

    def open_file(self):
        """
        打开文件
        :return:
        """
        self.file_name = askopenfilename(defaultextension = ".md")
        if self.file_name is not None:
            if not self.file_name.endswith(".md") and not self.file_name.endswith(".txt"):
                showerror("error", "不能打开该文件文件，目前此软件只能打开 .txt 和 .md 文件。")
                return
            self.root.title(os.path.basename(self.file_name))

            self.textarea.delete(1.0, END)

            with open(self.file_name, "r+", encoding = "utf-8") as file:
                self.textarea.insert(1.0 , file.read())

    def new_file(self):
        """
        新建文件
        :return:
        """
        self.file_name = None
        self.root.title("noting.md")
        self.textarea.delete(1.0, END)

    def save_file(self):
        """
        保存文件
        :return:
        """
        if self.file_name is not None:
            with open(self.file_name, "w") as file:
                # 全部重写
                file.write(self.textarea.get(1.0, END))
        else:
            self.save_as_file()

    def save_as_file(self):
        """
        另存为文件
        :return:
        """
        self.file_name = asksaveasfilename(initialfile = "demo.md", defaultextension = ".md")
        if self.file_name is not None:
            with open(self.file_name, "w") as file:
                file.write(self.textarea.get(1.0, END))
            self.root.title(os.path.basename(self.file_name))

    def undo(self):
        """
        撤销操作
        :return:
        """
        self.textarea.event_generate("<<Undo>>")

    def redo(self):
        """
        反撤销操作
        :return:
        """
        self.textarea.event_generate("<<Redo>>")

    def copy(self):
        """
        拷贝操作
        :return:
        """
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        """
        粘贴操作
        :return:
        """
        self.textarea.event_generate("<<Paste>>")

    def cut(self):
        """
        剪切操作
        :return:
        """
        self.textarea.event_generate("<<Cut>>")


if __name__ == '__main__':
    NoteApp().root.mainloop()
