# -*- coding: utf-8 -*-
from tkinter import *
import smtplib # Бібліотека для відправки електронної пошти зап протоколом SMTP
from email.mime.text import MIMEText # Модуль для выдправки звичайного тексту
from tkinter import messagebox # Відображення діалогів-повідомлень

sender = 'example.gui.i15@gmail.com' #відправник
password = 'W5mkw=#2rX_Y+-3%' #пароль для smtp-сервера
server = "smtp.gmail.com"
port = 587

# Діалог налаштувань
class MyDialog:
    def __init__(self, parent, server="", port=587, sender="", password=""): # Конструктор
        self.server = server
        self.port = port
        self.sender = sender
        self.password = password
        top = self.top = Toplevel(parent)
        top.transient(parent)    # Лише одне вікно в панелі задач
        top.grab_set()           # Зробити діалог модальним
        Label(top, text='SMTP server:').grid(row=0, sticky=E)
        Label(top, text='SMTP port:').grid(row=1, sticky=E)
        Label(top, text='Sender:').grid(row=2, sticky=E)
        Label(top, text='Password:').grid(row=3, sticky=E)
        self.eServer = Entry(top)
        self.eServer.insert(0, server)
        self.eServer.grid(row=0, column=1, sticky=E+W)
        self.ePort = Entry(top)
        self.ePort.insert(0, port)
        self.ePort.grid(row=1, column=1, sticky=E+W)
        self.eLogin = Entry(top)
        self.eLogin.insert(0, sender)
        self.eLogin.grid(row=2, column=1, sticky=E+W)
        self.ePassword = Entry(top)
        self.ePassword.insert(0, password)
        self.ePassword.grid(row=3, column=1, sticky=E+W)
        self.btnSubmit = Button(top, text='Ok', command=self.send)
        self.btnSubmit.grid(row=4, column=0, sticky=S+E+W)
        self.btnCancel = Button(top, text='Cancel', command=self.cancel)
        self.btnCancel.grid(row=4, column=1, sticky=S+E+W)
        Grid.columnconfigure(top, 1, weight=1)
        Grid.columnconfigure(top, 0, weight=1)
        
    def send(self): # Користувач натиснув кнопку "Ok"
        self.server = self.eServer.get()
        self.port = int(self.ePort.get())
        self.sender = self.eLogin.get()
        self.password = self.ePassword.get()
        self.top.destroy()
    
    def cancel(self): # Користувач натиснув кнопку "Cancel"
        self.top.destroy()

# Вивести питання про підтвердження виходу
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

#Функція відправки повідомлення
def send_message():
    recipients = eTo.get() #список отримувачів (якщо декілька, то розділяються комами)
    
    msg = MIMEText(tMessage.get('0.0',END)) # Текст листа
     
    msg['Subject'] = eSubject.get() # Тема листа
    msg['To'] = recipients # список отримувачів
    msg['From'] = sender # відправник
    
    print("Trying send mail...")
    # Відправка повідомлення
    try:
        with smtplib.SMTP(server, port) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, password)
            s.sendmail(sender, recipients, msg.as_string())
            s.close()
        messagebox.showinfo('Success', 'Email has been sent.') # Повідомлення про відправку листа
    except:
        messagebox.showerror("Unable to send the email", sys.exc_info()[0]) # Повыдомлення про помилку
        raise


#Функція налаштувань
def settings():
    # Використовувати глобальні змінні
    global server
    global port
    global sender
    global password
    # Створюємо діалог налаштувань
    settingsDialog = MyDialog(root, server=server, port=port, sender=sender, password=password)
    root.wait_window(settingsDialog.top) # Чекаємо завершення діалогу
    # Зчитуємо нові налаштування з діалогу
    server = settingsDialog.server 
    port = settingsDialog.port
    sender = settingsDialog.sender
    password = settingsDialog.password

#Створюємо головне вікно
root = Tk()
root.wm_title("Mail sender")
root.protocol("WM_DELETE_WINDOW", on_closing) # Обробка події закриття вікна

#Текстові написи біля полів вводу
Label(root, text="To:").grid(row=0, sticky=E)
Label(root, text="Subject:").grid(row=1, sticky=E)

#Поля вводу адреси й теми листа
eTo = Entry(root)
eSubject = Entry(root)

eTo.grid(row=0, column=1, sticky=E+W)
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
