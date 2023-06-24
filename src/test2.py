# create widget dynamically
# https://stackoverflow.com/questions/14804735/tkinter-how-can-i-dynamically-create-a-widget-that-can-then-be-destroyed-or-rem
from tkinter import *
root = Tk()
root.geometry('500x500')
superbut = Button(text='SUPER BUTTON')
outputtext = Text(width=25, height=10,bg='white', wrap=WORD)
outputtext.propagate(0)
superbut.pack(side=TOP)
outputtext.pack(side=BOTTOM)
dynamycs_button=[]
def create_on_button_click(event):
    but = Button(root, width=30)
    dynamycs_button.append(but)
    but.pack(side=TOP)
superbut.bind('<Button-1>', create_on_button_click)
changebut = Button(text='change')
changebut.pack(side=BOTTOM)
def changetext(event):
    #for i in range (len(dynamycs_button))
    #dynamycs_button[i]['text']='new'
    changebut['text'] = str(len(dynamycs_button))
changebut.bind('<Button-1>',changetext)
root.mainloop()

numbers = [1, 2, 3]
id(numbers)

numbers[0] = 10
numbers[1] = 20
numbers[2] = 30
numbers

id(numbers)