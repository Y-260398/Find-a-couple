# -*- coding: utf -8 -*-
import Tkinter



HEIGHT = 500
WIDTH = 800
window =  Tkinter.Tk()
window.title('Bubble Blaster')
image = Tkinter.PhotoImage(file = './222.gif')

class Test:
    def __init__(self, master):

        canvas = Tkinter.Canvas(master)
        canvas.grid(row = HEIGHT, column = WIDTH)

        photo = Tkinter.PhotoImage(file = './222.gif')

        canvas.create_image(0,0, image=photo)





root = Tkinter.Tk()
root.mainloop()
window.mainloop()
