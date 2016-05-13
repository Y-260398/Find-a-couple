# -*- coding: utf-8 -*-
from Tkinter import *
import smtplib # Бібліотека для відправки електронної пошти зап протоколом SMTP
from email.mime.text import MIMEText # Модуль для выдправки звичайного тексту
from Tkinter import messagebox # Відображення діалогів-повідомлень

# Вивести питання про підтвердження виходу
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

#Функція відправки повідомлення
def send_message():
    sender = 'example.gui.i15@gmail.com' #відправник
    gmail_password = 'W5mkw=#2rX_Y+-3%' #пароль для smtp-сервера
    recipients = eTo.get() #список отримувачів (якщо декілька, то розділяються комами)
    
    msg = MIMEText(tMessage.get('0.0',END)) # Текст листа
     
    msg['Subject'] = eSubject.get() # Тема листа
    msg['To'] = recipients # список отримувачів
    msg['From'] = sender # відправник
    
    print("Trying send mail...")
    # Відправка повідомлення
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, msg.as_string())
            s.close()
        messagebox.showinfo('Success', 'Email has been sent.') # Повідомлення про відправку листа
    except:
        messagebox.showerror("Unable to send the email", sys.exc_info()[0]) # Повыдомлення про помилку
        raise


#Заготовка функції налаштувань
def settings():
  print ("Settings")

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
