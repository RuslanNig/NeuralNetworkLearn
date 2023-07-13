import settings
import numpy as np
from tkinter import *
from tkinter import ttk


#create top general settings LabelFrame:
class TitleSettings: #class for title settings - amount of layers
    def __init__(self, master):
        self.top_set_frame = LabelFrame(master, text='General Settings', width=900, height = 50) #frame for input neurons layer
        self.top_set_frame.propagate(0)
        self.top_set_frame.pack(side='top',anchor=NW)
        self.ent_of_inputs = Entry(self.top_set_frame, width=15)
        self.button_inputs_create = Button(self.top_set_frame,width=25,text='Create Inputs')
        self.ent_of_layers_amount = Entry(self.top_set_frame,width=15)
        self.button_amount_create = Button(self.top_set_frame,width= 25,text="Create Layers")
        self.ent_of_inputs.pack(side=LEFT, padx=(5,5))
        self.button_inputs_create.pack(side = LEFT)
        self.ent_of_layers_amount.pack(side=LEFT, padx=(25,5))
        self.button_amount_create.pack(side=LEFT, padx=(5,5)) #button amount of layers cretion

#this class for creating LabelFrames for layers
class LayerFrame: #class for neuron layers amount
    def __init__(self,master,text_layer_number):
        self.inputs_list=[] #list of neurons for each layer
        self.frame_for_layer = LabelFrame(master, text = text_layer_number,width=100,height=400)
        self.frame_for_layer.propagate(0)
        self.frame_for_layer.pack(side=LEFT, anchor=NW)

        self.ent_of_neurons_amount = Entry(self.frame_for_layer,width=5)
        #we set buuton name as parameter of function __init__
        self.button_neuron_amount_create = Button(self.frame_for_layer,width=15,text="Cr. Nr-s", name = text_layer_number)
        self.button_neuron_amount_set = Button(self.frame_for_layer, width = 15, text='set')
        #this 'command' works fine: (read from: https://younglinux.info/tkinter/tkinter)
        self.button_neuron_amount_create['command'] = self.create_ent_neuron_of_layer
        self.button_neuron_amount_set['command'] = self.create_inputs_list_of_layer
        self.ent_of_neurons_amount.pack(side=TOP, anchor=NW)
        #button for neurons creation
        self.button_neuron_amount_create.pack(side=TOP,anchor=NW, padx=(5,5))
        self.button_neuron_amount_set.pack(side=TOP, anchor=NW )
        self.canvas_after_frame = Canvas(master, width=60, height=200)
        self.canvas_after_frame.pack(side=LEFT, anchor=NW)
        self.canvas_after_frame.create_line(10,10,30,30)
        self.list_of_thislayer_neurons_ent=[]
    #this function should correspont exatly this layer LabelFrame
    # def neuronCreate(event): #create object of class Block with content
    #     neuronQ = int(LayerFrame.ent_of_neurons_amount.get())
    #     for i in range (1,neuronQ+1):
    #         globals()[f'nrBlock_{i}'] = Block(LayerFrame.frame_for_layer,'Neuron '+str(i),'test')
    
    #try to create function for creation ENTRIES for neurons of layer
    #remember, we should use 'self' parameter
    #also Numpy array should be created
    def create_ent_neuron_of_layer(self):
        self.neurons_amount_of_this_layer = int(self.ent_of_neurons_amount.get())
        this_button_number = str(self.button_neuron_amount_create).split(".")[-1]
        #this works fine , it is just for testing:
        settings.glob_transit_textvar = this_button_number +"  "+ str(self.neurons_amount_of_this_layer)
        #list_of_neuronlayer is important global variable
        settings.list_of_neuronlayer[0]=1
        for i in range (1,self.neurons_amount_of_this_layer+1):
            ent_of_oneneuron = Entry(self.frame_for_layer, width=10)
            but_of_neuron_weights = Button(self.frame_for_layer, width=1, command=self.open_popup)
            ent_of_oneneuron.pack(side=TOP)
            but_of_neuron_weights.pack(side=TOP)

            self.list_of_thislayer_neurons_ent.append(ent_of_oneneuron)
        self.this_layer_testlab = Label(self.frame_for_layer, width=10, text = 'test')
        self.this_layer_testlab.pack(side=BOTTOM)
    
    def create_inputs_list_of_layer(self):
        for i in range(self.neurons_amount_of_this_layer):
            self.inputs_list.append(int(self.list_of_thislayer_neurons_ent[i].get()))
        inputs = np.array(self.inputs_list)
        self.this_layer_testlab['text'] = str(inputs)
        #self.this_layer_testlab['text'] = str(self.inputs_list)

    #this function call popup menu
    def open_popup(self):
        top = Toplevel()
        top.geometry("200x200")
        top.title("Child Window")
        Label(top, text= "input weights").pack(side=TOP)
        text = Text(top) 
        text.pack(side=TOP)

class InputsFrame: #class for input neurons frame
    def __init__(self, master,inputnodes):
        #create INPUTS LABELFRAME
        self.inodes = inputnodes
        self.master = master

        #CREATE CHECKBUTTONS
        # self.var1 = BooleanVar()    #for checkbutton
        # self.var1.set(0)            #for checkbutton
        # self.varst = StringVar() # for input neuron name Entry
        # self.varst.set('neuron_name')
        # self.check = Checkbutton(self.block_frame, variable=self.var1, command=self.changetext, onvalue = 1, offvalue = 0)
        
        #this Entry to set weight of input layer
        
        
        #self.check.pack(side = LEFT)
        
    def create_inputsframe(self):
        frame_for_inputlayer = LabelFrame(self.master, text = 'INPUTS',width=100,height=400)
        frame_for_inputlayer.propagate(0)
        frame_for_inputlayer.pack(side=LEFT, anchor=NW,padx=(5,25))
        ent = Entry(frame_for_inputlayer,width = 10)
        ent.pack(side=LEFT)


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


