from Tkinter import *
from Tkinter import Message
#from messagebox import *

def answer():
    message.showerror("Answer", "Sorry, no answer available")

def callback():
    if message.askyesno('Verify', 'Really quit?'):
        message.showwarning('Yes', 'Not yet implemented')
    else:
        message.showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()
