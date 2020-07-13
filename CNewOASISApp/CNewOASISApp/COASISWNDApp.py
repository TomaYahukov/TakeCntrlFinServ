from tkinter import *  #Load TKinker Windowing Class of Widgets
from COASISWindowCls import COASISWindow
from CHomoSapien import CHomoSapien
#***************************************************************
#Create a TKinker Window Class which Subclasses the Frame Class
#class COASISWindow(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        Frame.minsize(100,100)
#        self.master = master

class COASISWndApp(COASISWindow):
    ptrTkRootObj = None #root widget for TKinker
    strMyAppTitle = None
    strMyAppMsg = "Hello World from Pythod/TKinker!"
    ptrCurPersonObj = None #HomoSapien("Male", "English", True, True, True )
    ptrMyWndApp = None
    ptrDisplayLabel = None
    ptrPersonRecTxtWndObj = None #Frame window for Person Record Text
    ptrDataDirButWndObj = None #Record data directional Button Window/frame
    ptrExitButtonWndObj = None #Exit Button window/frme
    ptrNextButton = None #Moves forward to display Next Record
    ptrPrevButton = None #Button that takes us back to previous record
    ptrExitButton = None #Button that exis from App/mainLoop

    def __init__(self, ptrRoot, strAppTitle):
        #Initialize Window App
        ptrRoot.minsize(300, 300)
        self.ptrTkRootObj = ptrRoot #root = tk.Tk() #Starts TKinker by creating root widget
        self.ptrPersonRecTxtWndObj = COASISWindow(self.ptrTkRootObj) #Creates Window with Frame as Base Class and root as base object for Frame
        #**********************************************************************************************************************
        self.ptrPersonRecTxtWndObj.pack(side=TOP) #pack() function which automatically sets the widget according to the space available.
        #**********************************************************************************************************************
        # Set Minimum WinSize
        #self.ptrPersonRecTxtWndObj.minsize(100,100)
        self.ptrDataDirButWndObj = COASISWindow(self.ptrTkRootObj).pack(side=RIGHT)
        self.ptrExitButtonWndObj = COASISWindow(self.ptrTkRootObj).pack(side = BOTTOM)
        self.strMyAppTitle = strAppTitle
        #Set Winow Title
        self.ptrTkRootObj.wm_title(self.strMyAppTitle)
        #Display Window and enter App Loop
        #self.root.mainLoop()

    def vDisplayPersonRecord(self, ptrPerson):
         self.ptrCurPersonObj = ptrPerson
         #self.strWndApp
         self.ptrDisplayLabel = Label(self.ptrPersonRecTxtWndObj, text="Person Record Test Text_1\n").pack()
         self.ptrDisplayLabel = Label(self.ptrPersonRecTxtWndObj, text="Person Record Test Text_2\n").pack()
         self.ptrDisplayLabel = Label(self.ptrPersonRecTxtWndObj, text="Person Record Test Text_3\n").pack()
         self.ptrDisplayLabel = Label(self.ptrPersonRecTxtWndObj, text="Person Record Test Text_4\n").pack()
         self.ptrNextButton = Button(self.ptrDataDirButWndObj, text="Next", fg="black").pack(side = RIGHT)
         self.ptrPrevButton = Button(self.ptrDataDirButWndObj, text = "Prev", fg="black").pack(side = LEFT)
         self.ptrExitButton = Button(self.ptrExitButtonWndObj, text="Quit", fg="black", command=self.ptrTkRootObj.quit).pack()

def main():
    ptrMainWnd = Tk() #Creates the base widget/mainWindow widget usually called a root widget
    strMsg = "Hello World!"
    #Using the Tkinter base widget, create a Window Widget
    ptrMyAppObj = COASISWndApp(ptrMainWnd,  #Tk Base widget or mainWnd object 
                               "TJR HomoSapien OOPS Application") #App Main Window Title
    #Add a HomoSapien object, or PersonObj to internal Person Object Table
    ptrMyAppObj.ptrCurPersonObj = CHomoSapien("Male", "English", True, True, True )
    #Nonsense code
    ptrMyAppObj.ptrCurPersonObj.uiExit += 1

    #print(ptrPersonObj.strGetMySex())
    ptrMyAppObj.vDisplayPersonRecord(ptrMyAppObj.ptrCurPersonObj)

    #msg = "Hello World from Python!"
    #print(msg)
    #print(msg)
    x = [0, 1]
    i = 0
    i, x[i] = 1, 2
    #print(x)

    #print (__name__)
    #ptrMainWnd.minsize(400,400)
    ptrMainWnd.mainloop()
 
#The following will start app execution at main()
if __name__ == "__main__":
    main()
        
#if ptrPersonObj.exit < 1:
#    main()
    

