import myclassfile
from tkinter import *
root = Tk()

root.geometry('600x600') #https://younglinux.info/tkinter/window
ent_in = Entry(width=20)
but = Button(width=20,text='Enter neuronc quantity')
ent_in.pack()
but.pack()

def neuronCreate(event):
    neuronQ = int(ent_in.get())
    for i in range (1,neuronQ):
        globals()[f'nrBlock_{i}'] = myclassfile.Block(root,'Neuron '+str(i),'test')

but.bind('<Button-1>', neuronCreate)
root.mainloop()