#from curses import termattrs
import math
from pickle import TRUE
import tkinter as tk
from tkinter import Menu, ttk
from tkinter.messagebox import NO
from turtle import width
from unittest import result

from date.database import DB
import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

type=2


# Основной класс где содержится все функции главного меню
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2) #Создарние фрейма с заливкой, шириной и выравниванием
        toolbar.pack(side=tk.TOP, fill=tk.X)



        self.add_logo = tk.PhotoImage(file='assets/images/logo.gif')
        btn_logo = tk.Label(toolbar, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_logo)
        btn_logo.pack(side=tk.LEFT)

        if type == 1:
            self.delete_img = tk.PhotoImage(file='assets/images/delete.gif')
            btn_delete = tk.Button(toolbar, text='Удалить объявление   ', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
            btn_delete.pack(side=tk.RIGHT)

            self.update_img = tk.PhotoImage(file='assets/images/update.gif')
            btn_edit_dialog = tk.Button(toolbar, text='   Редактировать  ', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
            btn_edit_dialog.pack(side=tk.RIGHT)

            self.add_img = tk.PhotoImage(file='assets/images/add.gif')
            btn_open_dialog = tk.Button(toolbar, text="Добавить", command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
            btn_open_dialog.pack(side=tk.RIGHT)


            self.refresh_img = tk.PhotoImage(file='assets/images/refresh.gif')
            btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
            btn_refresh.place(x=math.floor(root.winfo_screenwidth() * 0.655))

            self.search_img = tk.PhotoImage(file='assets/images/search.gif')
            btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
            btn_search.place(x=math.floor(root.winfo_screenwidth() * 0.58))
        elif type==2:
            self.delete_img = tk.PhotoImage(file='assets/images/delete.gif')
            btn_delete = tk.Button(toolbar, text='Удалить вакансию   ', bg='#d7d8e0', bd=0, image=self.delete_img,
                                   compound=tk.TOP, command=self.delete_records)
            btn_delete.pack(side=tk.RIGHT)

            self.update_img = tk.PhotoImage(file='assets/images/update.gif')
            btn_edit_dialog = tk.Button(toolbar, text='   Редактировать  ', bg='#d7d8e0', bd=0, image=self.update_img,
                                        compound=tk.TOP, command=self.open_update_dialog)
            btn_edit_dialog.pack(side=tk.RIGHT)

            self.add_img = tk.PhotoImage(file='assets/images/add.gif')
            btn_open_dialog = tk.Button(toolbar, text="Добавить вакансию", command=self.open_dialog, bg='#d7d8e0', bd=0,
                                        compound=tk.TOP, image=self.add_img)
            btn_open_dialog.pack(side=tk.RIGHT)

            self.refresh_img = tk.PhotoImage(file='assets/images/refresh.gif')
            btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                    compound=tk.TOP, command=self.view_records)
            btn_refresh.place(x=math.floor(root.winfo_screenwidth() * 0.655))

            self.search_img = tk.PhotoImage(file='assets/images/search.gif')
            btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                                   compound=tk.TOP, command=self.open_search_dialog)
            btn_search.place(x=math.floor(root.winfo_screenwidth() * 0.58))
        else:
            self.refresh_img = tk.PhotoImage(file='assets/images/refresh.gif')
            btn_refresh = tk.Button(toolbar, text='          Обновить           ', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                    compound=tk.TOP, command=self.view_records)
            btn_refresh.pack(side=tk.RIGHT)

            self.search_img = tk.PhotoImage(file='assets/images/search.gif')
            btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                                   compound=tk.TOP, command=self.open_search_dialog)
            btn_search.pack(side=tk.RIGHT)


        self.tree = ttk.Treeview(self, columns=('id_user', 'type', 'contacts', 'description', 'payment', 'publication_date'), show='headings', height=150)

                    #Тут мы задаем ширину столбцов через вычисление ширины дисплея
        self.tree.column('id_user', width=math.floor(root.winfo_screenwidth() * 0.1), anchor=tk.CENTER)
        self.tree.column('type', width=math.floor(root.winfo_screenwidth() * 0.1), anchor=tk.CENTER)
        self.tree.column('contacts', width=math.floor(root.winfo_screenwidth() * 0.1), anchor=tk.CENTER)
        self.tree.column('description', width=math.floor(root.winfo_screenwidth() * 0.49), anchor=tk.CENTER)
        self.tree.column('payment', width=math.floor(root.winfo_screenwidth() * 0.1), anchor=tk.CENTER)
        self.tree.column('publication_date', width=math.floor(root.winfo_screenwidth() * 0.1), anchor=tk.CENTER)


                           #Верхние строки таблицы
        self.tree.heading('id_user', text='Имя пользователя')
        self.tree.heading('type', text='Тип')
        self.tree.heading('contacts', text='Контактные данные')
        self.tree.heading('description', text='Описание')
        self.tree.heading('payment', text='Оплата')
        self.tree.heading('publication_date', text='Дата подачи')



        mainmenu = Menu(root)         #Создание меню 
        root.config(menu=mainmenu)

        usermenu = Menu(mainmenu, tearoff=0)
        usermenu.add_command(label='Профиль')
        usermenu.add_command(label='Сменить Пользователя', command=self.change_user) # тут мы для Пользователя добавляем 2 лейбла с функциями

        usertype = Menu(mainmenu, tearoff=0)
        usertype.add_command(label='Добавить',command=self.open_dialog)
        usertype.add_command(label='Редактировать',command=self.open_update_dialog)
        usertype.add_command(label='Удалить',command=self.delete_records)
        usertype.add_command(label='Поиск',command=self.open_search_dialog)

        stat = Menu(mainmenu, tearoff=0)
        stat.add_command(label='Диаграмма1',command=self.stat_1)

        mainmenu.add_cascade(label='Пользователь', menu=usermenu)
        mainmenu.add_cascade(label='Функции', menu=usertype)
        mainmenu.add_command(label='О программе', command=self.info)
        mainmenu.add_cascade(label='Статистика',menu=stat)


        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview) #Скролл для таблицы с вызовом команды скрола
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)



    def records(self, id_user, type, contacts, description, payment, publication_date):                         #тут мы имеем обращение к базе данных дл вставки в таблицу наших переменных
        self.db.insert_data( id_user, type, contacts, description, payment, publication_date)
        self.view_records()

    def users(self, login, password,description,type):                         #тут мы имеем обращение к базе данных дл вставки в таблицу наших переменных
        self.db.insert_users( login, password,description, type)
        self.view_records()

    def get(self, login, password):
        global type
        self.db.c.execute('''SELECT * FROM users WHERE login = ?''', (login,))
        result = self.db.c.fetchone()
        if result[2] == password:
            if result[3] == '1':
                type = 1
                print(type)
                root.update()
            else:
                type = 2
        else:
            print("no")


    def update_record(self, id_user, type, contacts, description, payment, publication_date):
        self.db.c.execute('''UPDATE posts SET id_user=?, type=?, contacts=?, description=?, payment=?, publication_date=?, completion_date=?, status WHERE ID=?''',
                          (id_user, type, contacts, description, payment, publication_date, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT id_user, type, contacts, description, payment, publication_date FROM posts''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM posts WHERE id_user=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%',)
        self.db.c.execute('''SELECT * FROM posts WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


        #вызов дочерних классов
    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()
    
    def change_user(self):
        loginin()
    
    def info(self):
        info()

    def stat_1(self):
        stat1()

        #Дочерний класс где мы имеем создание окна так же лейбл, ввод данных, комбобох

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить объявление')
        self.geometry('1000x820+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Имя')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Тип')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Контактные данные')
        label_sum.place(x=50, y=110)
        label_sum = tk.Label(self, text='Описание')
        label_sum.place(x=50, y=140)
        label_sum = tk.Label(self, text='Оплата')
        label_sum.place(x=50, y=170)

        now=datetime.datetime.now()



        self.entry_id_user = ttk.Entry(self)
        self.entry_id_user.place(x=200, y=50)

        self.entry_contacts = ttk.Entry(self)
        self.entry_contacts.place(x=200, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=140)

        self.entry_payment = ttk.Entry(self)
        self.entry_payment.place(x=200, y=170)

        self.combobox = ttk.Combobox(self, values=[u'Вакансия', u'Исполнитель'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=300)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=300)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id_user.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_contacts.get(),
                                                                       self.entry_description.get(),
                                                                       self.entry_payment.get(),
                                                                       now))

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
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_id_user.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_contacts.get(),
                                                                          self.entry_description.get(),
                                                                          self.entry_payment.get()))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM posts WHERE id=?''',
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
        self.db = db

    def init_login(self):
        self.title('Регистрация')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Логин')
        label_description.place(x=50, y=50)
        label_sum = tk.Label(self, text='Пароль')
        label_sum.place(x=50, y=80)

        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=200, y=50)

        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.place(x=200, y=80)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=110)

        self.entry_type = ttk.Entry(self)
        self.entry_type.place(x=200, y=140)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)


        self.btn_ok = ttk.Button(self, text='Войти')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.users(self.entry_login.get(),
                                                                     self.entry_password.get(),
                                                                     self.entry_description.get(),
                                                                     self.entry_type.get()))

        self.grab_set()
        self.focus_set()



class loginin(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_loginin()
        self.view = app
        self.db = db



    def init_loginin(self, textt=0):
        self.title('Регистрация')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Логин')
        label_description.place(x=50, y=50)
        label_sum = tk.Label(self, text='Пароль')
        label_sum.place(x=50, y=80)



        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=200, y=50)

        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.place(x=200, y=80)

        btn_login = ttk.Button(self, text='reg', command=self.register)
        btn_login.place(x=140, y=170)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Войти')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.get(self.entry_login.get(),
                                                                   self.entry_password.get()
                                                                   ))

    def register(self):
        self.destroy()
        login()



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


class stat1(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.init_stat1()
        self.view = app
    def init_stat1(root):
        root.title('Диаграмма')

        data1 = {'Типы': ['Вак', 'Исп'],
                 'Значения': [1, 2]
                 }

        df1 = DataFrame(data1, columns=['Типы', 'Значения'])

        data2 = {'Неделя': [0, 1, 2, 3, 4],
                 'ЗП': [160000, 155000, 157000, 157000, 140000]
                 }
        df2 = DataFrame(data2, columns=['Неделя', 'ЗП'])

        data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
                 'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
                 }
        df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])


        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['Типы', 'Значения']].groupby('Типы').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Диаграмма отношения Вакансии/Исполнителя')

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Неделя', 'ЗП']].groupby('Неделя').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Средняя зарплата')

        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
        scatter3 = FigureCanvasTkAgg(figure3, root)
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(['Stock_Index_Price'])
        ax3.set_xlabel('Interest Rate')
        ax3.set_title('Interest Rate Vs. Stock Index Price')

        root.mainloop()




if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("JobHunter")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.state('zoomed')
    root.mainloop()

