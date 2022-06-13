# ***********************************************************************
# "Маленькое" подобие корпоративной информационной системы - КИС.
# Содержит в текстовом файле справочную информацию о
# сотруднике - фамилия, имя, отчество, должность, оклад, кабинет.
# Функционал - просмотреть имеющуюся информацию, сортировать информацию
# по алфавиту, добавить строку (запись), удалить строку (запись),
# поиск сотрудника по фамилии.
# ***********************************************************************

# from logging import root
from tkinter import *
from tkinter.ttk import Treeview
# from tkinter.messagebox import showinfo


# Входной поток, имитация файловой переменной
lst = [(1, 'Asur', 'Gete', 19000),
       (2, 'Bssr', 'Sete', 28000),
       (3, 'Tsur', 'Fete', 33000),
       (4, 'Nasur', 'Jete', 24000),
       (5, 'Fsur', 'Dete', 16000),
       (6, 'Wsur', 'QPete', 46000),
       (7, 'Esur', 'PPete', 77000),
       (8, 'Bssr', 'Sete', 28000),
       (9, 'Tsur', 'Fete', 33000),
       (10, 'Nasur', 'Jete', 24000),
       (11, 'Fsur', 'Dete', 16000),
       (12, 'Wsur', 'QPete', 46000),
       (13, 'Esur', 'PPete', 77000),
       (14, 'Asur', 'Gete', 19000),
       (15, 'Bssr', 'Sete', 28000),
       (16, 'Tsur', 'Fete', 33000),
       (17, 'Nasur', 'Jete', 24000),
       (18, 'Fsur', 'Dete', 16000),
       (19, 'Wsur', 'QPete', 46000),
       (20, 'Esur', 'PPete', 77000),
       (21, 'Bssr', 'Sete', 28000),
       (22, 'Tsur', 'Fete', 33000),
       (23, 'Nasur', 'Jete', 24000),
       (24, 'Fsur', 'Dete', 16000),
       (25, 'Wsur', 'QPete', 46000),
       (26, 'Esur', 'PPete', 77000)]


def func_add():
    win_add = Toplevel(root)
    win_add.geometry('350x210+300+300')
    win_add.title('Добавление новой записи')
    # win_add.grab_set() # фокус на окно
    # win_add.overrideredirect(1)

    def record_cancel():
        win_add.destroy()

    def record_add():
        print('GOOD')
        family = entr_family.get()
        name = entr_name.get()
        print(family, name)

    lbl_family = Label(win_add, text='Фамилия', padx=10).grid(
        row=0, column=0, sticky='w')
    lbl_name = Label(win_add, text='Имя', padx=10).grid(
        row=1, column=0, sticky='w')
    lbl_patronymic = Label(win_add, text='Отчество', padx=10).grid(
        row=2, column=0, sticky='w')
    lbl_post = Label(win_add, text='Должность', padx=10).grid(
        row=3, column=0, sticky='w')
    lbl_salary = Label(win_add, text='Оклад', padx=10).grid(
        row=4, column=0, sticky='w')
    lbl_office = Label(win_add, text='Кабинет', padx=10).grid(
        row=5, column=0, sticky='w')

    entr_family = Entry(win_add, width=25, textvariable=family).grid(
        row=0, column=1, padx=3, pady=3, sticky='e')
    entr_name = Entry(win_add, width=25).grid(row=1, column=1, padx=3, pady=3)
    entr_patronymic = Entry(win_add, width=25).grid(
        row=2, column=1, padx=3, pady=3)
    entr_post = Entry(win_add, width=25).grid(row=3, column=1, padx=3, pady=3)
    entr_salary = Entry(win_add, width=25).grid(
        row=4, column=1, padx=3, pady=3)
    entr_office = Entry(win_add, width=25).grid(
        row=5, column=1, padx=3, pady=3)

    btn_add_record = Button(win_add, text='Добавить', command=record_add).grid(
        row=6, column=0, padx=3, pady=3, sticky='e')
    btn_cancel_record = Button(win_add, text='Отменить', command=record_cancel).grid(
        row=6, column=1, padx=3, pady=3, sticky='w')


# ********************************************************
# Объявление виджетов
# ********************************************************
# основное окно
root = Tk()
root.title('Добро пожаловать в приложение')
root.geometry('965x250')

family = StringVar()
name = StringVar()
patronymic = StringVar()
post = StringVar()
salary = StringVar()
office = StringVar()


# Рамки
frm_list = Frame(root)
frm_func = Frame(root)
frm_tree = Frame(frm_list)
frm_scrol = Frame(frm_list)
# кнопки
btn_add = Button(frm_func, text='Добавить', width=15, command=func_add)
btn_edit = Button(frm_func, text='Редактировать', width=15)
btn_del = Button(frm_func, text='Удалить', width=15)
btn_sort = Button(frm_func, text='Сортировать', width=15)
btn_find = Button(frm_func, text='Поиск', width=15)
btn_out = Button(frm_func, text="Выход", width=15,
                 bg='blue', fg='white', command=root.quit)

# Таблица
heads = ['№', 'Фамилия', 'Имя', 'Оклад(рублей)']
table = Treeview(frm_tree, show='headings')
table['columns'] = heads
for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

for row in lst:
    table.insert('', END, values=row)
# Полоса прокрутки
scroll_pane = Scrollbar(frm_scrol, command=table.yview)
table.configure(yscrollcommand=scroll_pane.set)

# ********************************************************
# Размещение виджетов
# ********************************************************
# Рамки
frm_func.pack(side=LEFT)
frm_list.pack(side=LEFT, fill='x')
frm_tree.pack(side=LEFT, fill='x')
frm_scrol.pack(side=LEFT, fill='y')

# Кнопки
btn_add.pack()
btn_edit.pack()
btn_del.pack()
btn_sort.pack()
btn_find.pack()
btn_out.pack()
# Таблица
table.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Полоса прокрутки
scroll_pane.pack(side=LEFT, expand=YES, fill=BOTH)
# Текстовое поле

# непрерывный цикл
root.mainloop()
