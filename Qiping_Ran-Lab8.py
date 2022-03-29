# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:53:32 2022

@author: fra222
"""

from tkinter import *

class Draw(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Radio Buttons")
        self.grid()      
        self.canvas = Canvas(self, width = 300, height = 300, 
            bg = "white")
        self.canvas.grid(row = 0, column = 0)
        self.v1 = IntVar(value=0)
        self.v2 = IntVar(value=0)
        # Place buttons in a frame
        frame1 = Frame(self)
        frame1.grid(row = 1, column = 0)
        
        rectangle= Radiobutton(frame1, text = "Rectangle", 
                            command = self.displayRect, variable = self.v2, value = 1)
        rectangle.grid(row = 0, column = 0)

        oval = Radiobutton(frame1, text = "Oval", 
                               
                               command = self.displayOval, variable = self.v2, value = 2)
        oval.grid(row = 0, column = 1)
        
        filled=Checkbutton(frame1,text="filled",variable = self.v1, onvalue=1,offvalue=0,command = self.processRadiobutton)
        filled.grid(row = 0, column = 2)
        
        clear = Button(frame1, text = "Clear", 
            command = self.clearCanvas)
        clear.grid(row = 0, column = 3)

    def processRadiobutton(self):
        pass
        # self.v1.get()=1
        # if self.v1.get() ==0:
        #     self.canvas.create_rectangle["fill"]=""
        # else:
        #     self.canvas.create_rectangle["fill"]="red"
        # if self.v1.get() ==0:
        #     self.canvas.create_oval["fill"]=""
        # else:
        #     self.canvas.create_oval["fill"]="red"
        
            
        
    def clearCanvas(self):
        self.canvas.delete(ALL)
        self.v1.set(0)
        self.v2.set(0)
     # Display a rectangle
    def displayRect(self):
        if self.v1.get() ==0:
            self.canvas.create_rectangle(50, 50, 250, 250, tags = "rect",fill = "")
        else:
            self.canvas.create_rectangle(50, 50, 250, 250, tags = "rect",fill = "red")
    def displayOval(self):
        if self.v1.get() ==0:
            self.canvas.create_oval(50, 100, 250, 250, fill = "",tags = "oval")
        else:
            self.canvas.create_oval(50, 100, 250, 250, fill = "yellow",tags = "oval")
        

def main():
    Draw().mainloop()

main()