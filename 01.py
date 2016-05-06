# -*- coding: utf-8 -*-
from tkinter import *

#Заготовка функції відправки повідомлення
def send_message():
   print("Send message")

#Заготовка функції налаштувань
def settings():
  print ("Settings")

#Створюємо головне вікно
root = Tk()
root.wm_title("Mail sender")

#Текстові написи біля полів вводу
Label(root, text="To:").grid(row=0, sticky=E)
Label(root, text="Subject:").grid(row=1, sticky=E)

#Поля вводу адреси й теми листа
eFrom = Entry(root)
eSubject = Entry(root)

eFrom.grid(row=0, column=1, sticky=E+W)
eSubject.grid(row=1, column=1, sticky=E+W)

#Книпки відправки повідомлення й налаштувань
Button(root, text='Settings', command=settings).grid(row=3, column=0, sticky=N+S+E+W, pady=4)
Button(root, text='Send', command=send_message).grid(row=3, column=1, sticky=N+S+E+W, pady=4)

#Текстове поле для вводу тіла листа
tMessage= Text(root, height=20, width=50)
scroll = Scrollbar(root, command=tMessage.yview)#Полоса прокрутки
tMessage.configure(yscrollcommand=scroll.set)
tMessage.insert(END,'Write your message here\n')

tMessage.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W)
scroll.grid(row=2, column=2, sticky=N+S)

#Налаштування масштабування вікна
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

root.mainloop()
