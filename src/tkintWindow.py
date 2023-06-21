import myclassfile
from tkinter import *
root = Tk()
root.geometry('1200x700') #https://younglinux.info/tkinter/window

#create top general settings LabelFrame:
top_set_frame = LabelFrame(root, text='General Settings', width=500, height = 50) #frame for input neurons layer
top_set_frame.propagate(0)
top_set_frame.pack(side='top',anchor=NW)
ent_of_layers_amount = Entry(top_set_frame,width=15)
button_amount_create = Button(top_set_frame,width=15,text="Create Layers")
Label(top_set_frame,text='Layers Amount', width=20).pack(side = LEFT)
ent_of_layers_amount.pack(side=LEFT)
button_amount_create.pack(side=LEFT, padx=(5,5))

#block of layers amount creation
class LayerFrame: #class for neuron layers amount
    def __init__(self, master):
        self.frame_fo_layer = LabelFrame(master, text = "some text")
        self.label_test = Label(self.frame_fo_layer, text="test text")
        self.frame_fo_layer.pack(side=RIGHT)
        self.label_test.pack()
def layer_amount_create(event):
    layer_amount = int(ent_of_layers_amount.get())
    for i in range(1,layer_amount+1):
        globals()[f'neuron_layer_{i}'] = LabelFrame(root)
button_amount_create.bind('<Button-1>', layer_amount_create)
#end of layers amount cretion

superFrame = LabelFrame(root, text='first input layer', width=305, height = 400) #frame for input neurons layer
ent_in = Entry(superFrame, width=20)
but = Button(superFrame, width=20,text='Enter neuronc quantity')
superFrame.propagate(0)                 #look my pres "Python graphiks Tkinter"
superFrame.pack(side='top',anchor=NW)   #look my pres "Python graphiks Tkinter"
ent_in.pack()
but.pack()

def neuronCreate(event): #create class Block wiwh content
    neuronQ = int(ent_in.get())
    for i in range (1,neuronQ+1):
        globals()[f'nrBlock_{i}'] = myclassfile.Block(superFrame,'Neuron '+str(i),'test')

but.bind('<Button-1>', neuronCreate)
root.mainloop()