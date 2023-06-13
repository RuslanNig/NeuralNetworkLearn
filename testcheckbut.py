from tkinter import *
root = Tk()
superFrame1 = LabelFrame(root, text="SUPERFRAME 1")
f_top = LabelFrame(superFrame1,text='frame 1')
f_bot = LabelFrame(root,text='frame 2')
l1 = Label(f_top, width=7, height=4,
           bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4,
           bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4,
           bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4,
           bg='lightblue', text="4")
superFrame1.pack() 
f_top.pack(side=LEFT)
f_bot.pack(side = LEFT)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)
 
root.mainloop()