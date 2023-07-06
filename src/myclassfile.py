from tkinter import *

#create top general settings LabelFrame:
class TitleSettings: #class for title settings - amount of layers
    def __init__(self, master):
        self.top_set_frame = LabelFrame(master, text='General Settings', width=700, height = 50) #frame for input neurons layer
        self.top_set_frame.propagate(0)
        self.top_set_frame.pack(side='top',anchor=NW)
        self.ent_of_layers_amount = Entry(self.top_set_frame,width=15)
        self.ent_max_neurons_of_layer = Entry(self.top_set_frame, width=15)
        self.button_amount_create = Button(self.top_set_frame,width= 35,text="Create Layers")
        Label(self.top_set_frame,text='Layers Amount', width=20).pack(side = LEFT)
        self.ent_of_layers_amount.pack(side=LEFT)
        Label(self.top_set_frame,text='MAX neurons in one layer', width=20).pack(side=LEFT)
        self.ent_max_neurons_of_layer.pack(side=LEFT)
        #button amount of layers cretion
        self.button_amount_create.pack(side=LEFT, padx=(5,5))

#this class for creating LabelFrames for layers
class LayerFrame: #class for neuron layers amount
    def __init__(self,master,text_layer_number):
        self.frame_for_layer = LabelFrame(master, text = text_layer_number,width=100,height=40)
        self.frame_for_layer.propagate(0)
        self.frame_for_layer.pack(side=LEFT, anchor=NW)

        self.ent_of_neurons_amount = Entry(self.frame_for_layer,width=5)
        self.button_neuron_amount_create = Button(self.frame_for_layer,width=15,text="Cr. Nr-s")
        self.ent_of_neurons_amount.pack(side=LEFT)
        #button for neurons creation
        self.button_neuron_amount_create.pack(side=LEFT,padx=(5,5))

        self.canvas_after_frame = Canvas(master, width=60, height=200)
        self.canvas_after_frame.pack(side=LEFT, anchor=NW)
        self.canvas_after_frame.create_line(10,10,30,30)
    #this function should correspont exatly this layer LabelFrame
    def neuronCreate(event): #create object of class Block with content
        neuronQ = int(LayerFrame.ent_of_neurons_amount.get())
        for i in range (1,neuronQ+1):
            globals()[f'nrBlock_{i}'] = Block(LayerFrame.frame_for_layer,'Neuron '+str(i),'test')
    
    #try to create function for cretion neurons of layer without class
    def create_neuron_of_layer(event):
        neuron_amount = int(LayerFrame.ent_of_neurons_amount.get())
        layer_neurons_list = []
        neuron_frame = LabelFrame(text='neuron')
        neuron_ent = Entry(width=5)
        layer_neurons_list.append(neuron_frame)
        layer_neurons_list.append(neuron_ent)
        neuron_frame.pack()

class Block: #класс для входных нейронов
    def __init__(self, master, name_fr,labtext):
        self.block_frame = LabelFrame(master, text = name_fr)
        self.var1 = BooleanVar()    #for checkbutton
        self.var1.set(0)            #for checkbutton
        self.varst = StringVar() # for input neuron name Entry
        self.varst.set('neuron_name')
        self.check = Checkbutton(self.block_frame, variable=self.var1, command=self.changetext, onvalue = 1, offvalue = 0)
        #this Entry to set weight of input layer
        self.ent = Entry(self.block_frame,width = 10)
        #this Label just to control of Checkmbutton changing value
        self.nlab = Label(self.block_frame,text=labtext, width=10)
        self.block_frame.pack()
        #next is Entry to show input signal some name:
        Entry(self.block_frame,text='neuron name', bg = 'grey', textvariable=self.varst, width=20).pack(side = LEFT)
        self.check.pack(side = LEFT)
        self.ent.pack(side=LEFT)
        self.nlab.pack(side=LEFT)
    def changetext(self): #this function change text in label in accordance with checkbutton
        self.nlab['text'] = self.var1.get()

class NeyronOfLayer: #класс для входных нейронов
    def __init__(self, master, name_fr,labtext):
        self.block_frame = LabelFrame(master, text = name_fr)
        self.var1 = BooleanVar()    #for checkbutton
        self.var1.set(0)            #for checkbutton
        self.varst = StringVar() # for input neuron name Entry
        self.varst.set('neuron_name')
        self.check = Checkbutton(self.block_frame, variable=self.var1, command=self.changetext, onvalue = 1, offvalue = 0)
        #this Entry to set weight of input layer
        self.ent = Entry(self.block_frame,width = 10)
        #this Label just to control of Checkmbutton changing value
        self.nlab = Label(self.block_frame,text=labtext, width=10)
        self.block_frame.pack()
        #next is Entry to show input signal some name:
        Entry(self.block_frame,text='neuron name', bg = 'grey', textvariable=self.varst, width=20).pack(side = LEFT)
        self.check.pack(side = LEFT)
        self.ent.pack(side=LEFT)
        self.nlab.pack(side=LEFT)
    def changetext(self): #this function change text in label in accordance with checkbutton
        self.nlab['text'] = self.var1.get()