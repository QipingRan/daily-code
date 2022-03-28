# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:28:54 2022

@author: fra22
"""

from tkinter import *
import numpy as np
import itertools, random
class Memory_Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Memory Game")
        self.grid()
        
        self.rows=Label(self,text="rows:")
        self.rows.grid(row=0,column=0)
        self.rowsVal=IntVar()
        self.rowsVal.set(2)
        self.rowsEntry=Entry(self,textvariable=self.rowsVal)
        self.rowsEntry.grid(row=0,column=1)
        
        self.rows=Label(self,text="columns:")
        self.rows.grid(row=0,column=2)
        self.columnsVal=IntVar()
        self.columnsVal.set(2)
        self.rowsEntry=Entry(self,textvariable=self.columnsVal)
        self.rowsEntry.grid(row=0,column=3)
        
        self.button=Button(self,text="1.Creat matrix",command=self.creat_matrix)
        self.button.grid(row=0,column=4,columnspan=2)
        
        #1
        self.rows=Label(self,text="x1:")
        self.rows.grid(row=1,column=0)
        self.x1Val=DoubleVar()
        self.x1Val.set(1)
        self.rowsEntry=Entry(self,textvariable=self.x1Val)
        self.rowsEntry.grid(row=1,column=1)
        
        self.rows=Label(self,text="y1:")
        self.rows.grid(row=1,column=2)
        self.y1Val=DoubleVar()
        self.y1Val.set(1)
        self.rowsEntry=Entry(self,textvariable=self.y1Val)
        self.rowsEntry.grid(row=1,column=3)
        #2
        self.rows=Label(self,text="x2:")
        self.rows.grid(row=2,column=0)
        self.x2Val=DoubleVar()
        self.x2Val.set(2)
        self.rowsEntry=Entry(self,textvariable=self.x2Val)
        self.rowsEntry.grid(row=2,column=1)
        self.rows=Label(self,text="y2:")
        self.rows.grid(row=2,column=2)
        self.y2Val=DoubleVar()
        self.y2Val.set(2)
        self.rowsEntry=Entry(self,textvariable=self.y2Val)
        self.rowsEntry.grid(row=2,column=3)
        #3
        self.button=Button(self,text="2.show output",command=self.show_output)
        self.button.grid(row=1,column=4,columnspan=2)
        #4
        self.button=Button(self,text="3.continue",command=self.to_continue)
        self.button.grid(row=2,column=4,columnspan=2)
    
    def creat_matrix(self):
        rows=self.rowsVal.get()
        columns=self.columnsVal.get()
        mid=rows*columns//2
        deck = []
        for i in range(1,mid+1):
            deck.append(str(i))
            deck.append(str(i))
        random.shuffle(deck)
        print("The new matrix is: ")
        print(deck)
        print()
    def to_continue(self):
        rows=self.rowsVal.get()
        columns=self.columnsVal.get()
        x1=self.x1Val.get()
        y1=self.y1Val.get()
        x2=self.x2Val.get()
        y2=self.y2Val.get()
        x1=int(x1)
        y1=int(y1)
        x2=int(x2)
        y2=int(y2)
        
        if b[x1-1][y1-1]==b[x2-1][y2-1]:
            a[x1-1][y1-1]=b[x1-1][y1-1]
            a[x2-1][y2-1]=b[x2-1][y2-1]
            print(a)

            print(b)
        else:
            string="Not an identical pair. Found:"+ str(b[x1-1][y1-1]) +" at"+"("+str(x1)+","+str(y1)+")" +"and:"+str(b[x2-1][y2-1]) +" at"+"("+str(x2)+","+str(y2)+")"
            
            print(string)
        a1=a.tolist()
        b1=b.tolist()
        if a1==b1:
            print("Congratulation!Game OVer!!!")
        else:
            print("Continue to input.Game is not over yet!")
        print()
            
    def show_output(self):
        global a
        global b
        print("show output command: ")
        rows=self.rowsVal.get()
        columns=self.columnsVal.get()
        mid=rows*columns//2
        deck = []
        for i in range(1,mid+1):
            deck.append(str(i))
            deck.append(str(i))
        random.shuffle(deck)
        
        m=[]
        while deck!=[]:
            m.append(deck[:columns])
            deck=deck[columns:]
      
        
        #output
        output = []
        for i in range(1,mid+1):
            output.append('*')
            output.append('*')
       
        n=[]
        while output!=[]:
            n.append(output[:columns])
            output=output[columns:]
       
        
        a = np.array(n)
        b = np.array(m)
        print("output will shows like:")
        for line in a:
            print ('  '.join(map(str, line)))
        print("decks after shuffle:")
        for line in b:
            print ('  '.join(map(str, line)))
       
        b1=b.tolist()
        # print(b1)
        print()
       
      
        # while True:
        #     x1=self.x1Val.get()
        #     y1=self.y1Val.get()
        #     x2=self.x2Val.get()
        #     y2=self.y2Val.get()
        #     x1=int(x1)
        #     y1=int(y1)
        #     x2=int(x2)
        #     y2=int(y2)
        #     if b[x1-1][y1-1]==b[x2-1][y2-1]:
        #         a[x1-1][y1-1]=b[x1-1][y1-1]
        #         a[x2-1][y2-1]=b[x2-1][y2-1]
        #         print(a)
    
        #         print(b)
        #     else:
        #         string="Not an identical pair. Found:"+ str(b[x1-1][y1-1]) +" at"+"("+str(x1)+","+str(y1)+")" +"and:"+str(b[x2-1][y2-1]) +" at"+"("+str(x2)+","+str(y2)+")"
                
        #         print(string)
            # a1=a.tolist()
            # b1=b.tolist()
            # if a1==b1:
            #     break
        # print("Congratulation!Game OVer!!!")
       
    
    
    
def main():
    Memory_Game().mainloop()
main()