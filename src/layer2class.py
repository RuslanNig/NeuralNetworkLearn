from tkinter import *
class LayerTwoBlock: #класс для входных нейронов
    def __init__(self, master, name_fr,labtext):
        self.block_frame = LabelFrame(master, text = name_fr)
        self.var1 = BooleanVar() #for checkbutton
        self.var1.set(0)
        self.varst = StringVar() # for input neuron name Entry
        self.varst.set('neuron_name')
        self.check = Checkbutton(self.block_frame, variable=self.var1, command=self.changetext, onvalue = 1, offvalue = 0)
        #this Entry to set weight of input layer
        self.ent = Entry(self.block_frame,width = 10)
        #this Label just to control of Checkmbutton changing value
        self.nlab = Label(self.block_frame,text=labtext, width=10)
        self.block_frame.pack()
        #next is Entry to show input signak=l some name:
        Entry(self.block_frame,text='neuron name', bg = 'grey', textvariable=self.varst, width=20).pack(side = LEFT)
        self.check.pack(side = LEFT)
        self.ent.pack(side=LEFT)
        self.nlab.pack(side=LEFT)
    def changetext(self): #this function change text in label in accordance with checkbutton
        self.nlab['text'] = self.var1.get()