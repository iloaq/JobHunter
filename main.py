import math
import tkinter as tk
from tkinter import Menu, ttk
from tkinter.messagebox import NO
from turtle import width
from date.database import DB
import textwrap

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_logo = tk.PhotoImage(file='assets/images/logo.gif')
        btn_logo = tk.Button(toolbar, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_logo)
        btn_logo.pack(side=tk.LEFT)

        self.add_img = tk.PhotoImage(file='assets/images/add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить объявление', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.RIGHT)

        self.update_img = tk.PhotoImage(file='assets/images/update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='   Редактировать  ', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.RIGHT)

        self.delete_img = tk.PhotoImage(file='assets/images/delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить объявление', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.RIGHT)

        self.search_img = tk.PhotoImage(file='assets/images/search.gif')
        btn_search = tk.Button(toolbar, text='          Поиск         ', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.RIGHT)

        self.refresh_img = tk.PhotoImage(file='assets/images/refresh.gif')
        btn_refresh = tk.Button(toolbar, text='           Обновить          ', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), displaycolumns=('ID', 'costs', 'total', 'description'), show='headings', height=150)

        self.tree.column('ID', width=math.floor(root.winfo_screenwidth() * 0.01), anchor=tk.CENTER)
        self.tree.column('description', width=math.floor(root.winfo_screenwidth() * 0.693), anchor=tk.CENTER)
        self.tree.column('costs', width=math.floor(root.winfo_screenwidth() * 0.09), anchor=tk.CENTER)
        self.tree.column('total', width=math.floor(root.winfo_screenwidth() * 0.2), anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Описание')
        self.tree.heading('costs', text='Тип')
        self.tree.heading('total', text='Контактные данные')

        root.update()

        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        usermenu = Menu(mainmenu, tearoff=0)
        usermenu.add_command(label='Профиль')
        usermenu.add_command(label='Сменить Пользователя', command=self.change_user)

        mainmenu.add_cascade(label='Пользователь', menu=usermenu)
        mainmenu.add_command(label='О программе', command=self.info)


        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)



    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def update_record(self, description, costs, total):
        self.db.c.execute('''UPDATE finance SET description=?, costs=?, total=? WHERE ID=?''',
                          (description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM finance WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%',)
        self.db.c.execute('''SELECT * FROM finance WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()
    
    def change_user(self):
        login()
    
    def info(self):
        info()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить объявление')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Описание')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Тип')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Контактные данные')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u'Вакансия', u'Исполнитель'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать объявление')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM finance WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.entry_description.insert(0, row[1])
        if row[2] != 'Доход':
            self.combobox.current(1)
        self.entry_money.insert(0, row[3])


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class login(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_login()
        self.view = app

    def init_login(self):
        self.title('Авторизация')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Логин')
        label_description.place(x=50, y=50)
        label_sum = tk.Label(self, text='Пароль')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self, show="*")
        self.entry_money.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Войти')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class info(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_info()
        self.view = app
    
    def init_info(self):
        self.title('о программе')
        self.geometry('500x350')
        self.resizable(False, False)

        label_name=tk.Label(self, text="JobHunter",font=("Arial",25))
        label_name.place(x=175, y= 10)

        label_info=tk.Label(self, text="Программа была сделанна с помощью языка программирования Python,\n с использованием Tkinter")
        label_info.place(x=10, y=70)

        label_name_group= tk.Label(self, text="Кальяскаров Арман АПО-19\n Тарасюк Андрей АПО-19\n Исенгужин Роман АПО-19\n Селимгерей Нурболат АПО-19")
        label_name_group.place(x=10, y= 110)

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("JobHunter")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.state('zoomed')
    root.mainloop()

