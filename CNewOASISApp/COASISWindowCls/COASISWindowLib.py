from tkinter import *  #Load TKinker Windowing Class of Widgets
#***************************************************************
#Create a TKinker Window Class which Subclasses the Frame Class
class COASISWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
#        Frame.minsize(100,100)
        self.master = master
