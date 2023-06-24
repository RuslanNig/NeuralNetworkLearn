#read this carefully: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
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
    layer_amount = int(title.ent_of_layers_amount.get())
    global list_of_layerframe #this variable is global
    list_of_layerframe = []
    for i in range(1,layer_amount+1):
        #looks like globals no needed
        #globals()[f'neuron_layer_{i}'] = myclassfile.LayerFrame(root, 'Layer № '+ str(i))
        layer_frame = myclassfile.LayerFrame(root, 'Layer № ' + str(i))
        list_of_layerframe.append(layer_frame)

def testbutton_func(event):
    labout['text'] = str(list_of_layerframe[2])

title.button_amount_create.bind('<Button-1>', layer_amount_create)
testbutton.bind('<Button-1>', testbutton_func)
root.mainloop()

#end of all code
