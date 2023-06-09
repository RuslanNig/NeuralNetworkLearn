from tkinter import *
class Block:
    def __init__(self, master, name_fr):
        self.block_frame = LabelFrame(master, text = name_fr)
        self.check = Checkbutton(self.block_frame)
        self.ent = Entry(self.block_frame,width = 10)
        self.block_frame.pack()
        self.check.pack(side = LEFT)
        self.ent.pack(side=LEFT)
root = Tk()
root.geometry('600x600') #https://younglinux.info/tkinter/window
ent_in = Entry(width=20)
but = Button(width=20,text='Enter neuronc quantity')
ent_in.pack()
but.pack()

def neuronCreate(event):
    neuronQ = int(ent_in.get())
    for i in range (1,neuronQ):
        globals()[f'nrBlock_{i}'] = Block(root,'Neuron '+str(i))

but.bind('<Button-1>', neuronCreate)
root.mainloop()