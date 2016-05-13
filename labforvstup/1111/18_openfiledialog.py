from Tkinter import *
from Tkinter import FileType

def callback():
    name= FileType.askopenfilename()
    print (name)
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()
