from tkinter import *

class LayerFrame: #class for neuron layers amount
    def __init__(self):
        self.frame_for_layer = LabelFrame(root, text = "some text",width=100,height=40)
        self.frame_for_layer.propagate(0)
        self.label_test = Label(self.frame_for_layer, text="test text")
        self.frame_for_layer.pack(side=LEFT)
        self.label_test.pack()

root = Tk()
root.geometry('1300x700')
top_set_frame = LabelFrame(root, text='General Settings', width=500, height = 50) #frame for input neurons layer
top_set_frame.propagate(0)
top_set_frame.pack(side=RIGHT,anchor=NW)
ent_of_layers_amount = Entry(top_set_frame,width=15)
button_amount_create = Button(top_set_frame,width=15,text="Create Layers")
lab_amount = Label(top_set_frame,text='Layers Amount', width=20)
lab_amount.pack(side=LEFT)
ent_of_layers_amount.pack(side=LEFT)
button_amount_create.pack(side=LEFT, padx=(5,5))


def layer_amount_create(event):
    layer_amount = int(ent_of_layers_amount.get())
    lab_amount['text'] = ent_of_layers_amount.get()
    for i in range(1,layer_amount+1):
        globals()[f'neuron_layer_{i}'] = LayerFrame() #create objects of class LayerFrame

button_amount_create.bind('<Button-1>', layer_amount_create)

root.mainloop()