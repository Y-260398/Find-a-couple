# -*- coding: utf -8 -*-

#імпорт модулю tkinter
import Tkinter


#розміри ігрового поля
HEIGHT = 500
WIDTH = 800
#створення головного вікна
window = Tkinter.Tk()
window.title('Bubble Blaster')
#створення об’єкта Canvas для відображення ігрового поля
c = Tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
c.pack()

# запускаємо головний цикл вікна (щоб воно лишалося на екрані)
window.mainloop()
