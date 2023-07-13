#read this carefully: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
import settings
import myclassfile
import numpy as np
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('1200x500+50+50') #https://younglinux.info/tkinter/window

#auxiliary button label for TESTING in the bottom of the root Tk()
labout = Label(root, text="auxiliary text window", width=300, bg='green')
testbutton = Button(text='TEST BUTTON', name='testbutton')
labout.pack(side=BOTTOM)
testbutton.pack(side=BOTTOM)

# #create TITLE with general settings - amount of layers:
title = myclassfile.TitleSettings(root)

def layer_amount_create(event):
    
    #CREATE INPUT LAYER FRAME
    #read amount of input neurons in input layer:
    settings.inputs_neurons_amount_glob = int(title.ent_of_inputs.get())
    input_frame = myclassfile.InputsFrame(root, settings.inputs_neurons_amount_glob)
    input_frame.create_inputsframe()
    
    #read amount of layers and max amount neurons in layer
    settings.layer_amount = int(title.ent_of_layers_amount.get())
    #settings.max_neurons_inlayer = int(title.ent_max_neurons_of_layer.get())
    global list_of_layerframe #this variable is global
    list_of_layerframe = []
    
    #create hidden_frame objects
    for i in range(1,settings.layer_amount+1):
        #looks like globals no needed
        #globals()[f'neuron_layer_{i}'] = myclassfile.LayerFrame(root, 'Layer № '+ str(i))
        #create layer_frame and array corresponding layer_frame
        layer_frame = myclassfile.LayerFrame(root, 'layer_№ ' + str(i))
        layer_array = np.zeros([])
        list_of_layerframe.append(layer_frame) #remember, pack already in Class
        settings.list_of_neuronlayer.append(layer_array)

#just to output something
def testbutton_func(event):
    #labout['text'] = str(list_of_layerframe[2])
    #labout['text'] = str(settings.list_of_neuronlayer[2])
    #labout['text'] = list_of_layerframe[0].frame_for_layer.cget('text') #this work fine
    labout['text'] = str(list_of_layerframe[3].button_neuron_amount_create) #this work fine
    #this just test how event.widget works:
    #labout['text'] = str(event.widget).split(".")[-1] #this work fine, shows 'name' of 'testbutton'

#function to get name of the widget
def get_widget_name(event):
    #settings.glob_transit_textvar = event.widget
    labout['text'] = settings.glob_transit_textvar


#this button click creates the desired number of layers
title.button_amount_create.bind('<Button-1>', layer_amount_create)
#testbutton.bind('<Button-1>', testbutton_func)
testbutton.bind('<Button-1>', get_widget_name) #get_widget_name - it's my function

root.mainloop()

#end of all code
