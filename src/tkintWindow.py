#read this carefully: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
import settings
import myclassfile
import numpy as np
from tkinter import *
root = Tk()
root.geometry('1200x700') #https://younglinux.info/tkinter/window

#auxiliary button label for TESTING in the bottom of the Tk()
labout = Label(root, text="auxiliary text window", width=300, bg='green')
testbutton = Button(text='TEST BUTTON')
labout.pack(side=BOTTOM)
testbutton.pack(side=BOTTOM)

# #create TITLE with general settings - amount of layers:
title = myclassfile.TitleSettings(root)

def layer_amount_create(event):
    #read amount of layers and max amount neurons in layer
    settings.layer_amount = int(title.ent_of_layers_amount.get())
    settings.max_neurons_inlayer = int(title.ent_max_neurons_of_layer.get())
    global list_of_layerframe #this variable is global
    list_of_layerframe = []
    settings.neurons_array = np.resize(settings.neurons_array,(settings.layer_amount,settings.max_neurons_inlayer))
    for i in range(1,settings.layer_amount+1):
        #looks like globals no needed
        #globals()[f'neuron_layer_{i}'] = myclassfile.LayerFrame(root, 'Layer № '+ str(i))
        layer_frame = myclassfile.LayerFrame(root, 'Layer № ' + str(i))
        list_of_layerframe.append(layer_frame)

#just to output something
def testbutton_func(event):
    #labout['text'] = str(list_of_layerframe[2])
    labout['text'] = str(settings.neurons_array)

#this button click creates the desired number of layers
title.button_amount_create.bind('<Button-1>', layer_amount_create)
testbutton.bind('<Button-1>', testbutton_func)
root.mainloop()

#end of all code
