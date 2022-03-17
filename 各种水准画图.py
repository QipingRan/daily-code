# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:29:38 2022

@author: fra22
"""
#利用python的matplotlib来画图

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw_sin():
    x=np.arange(-12.1,12.1,0.1)
    y=np.sin(x) #画sin函数
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k') #画y轴
    ax.axvline(x=0, color='k') #画x轴
    
    plt.plot(x,y)

#画画 y1 = x^2 以及y2 = x^3    
def square_x_function():
    x=np.arange(-120.0,120.0,0.1)
    y=np.power(x,3) #画x的立方函数
    plt.plot(x,y)
    
def draw_directly():
    x = np.linspace(0.2,10,100)
    fig, ax = plt.subplots()
    ax.plot(x, 1/x)
    ax.plot(x, np.log(x))
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    ax.axhline(y=0, color='k') #画y轴
    ax.axvline(x=0, color='k') #画x轴
    
    
#画比较高的函数画x + y + x2+y2 = 1
def high_order_function():
    X = np.arange(-10,10,0.01)
    Y = np.arange(-10,10,0.01)
    cordinates = [(x, y) for x in X for y in Y]
    x_cord, y_cord = zip(*cordinates)
    data = pd.DataFrame({"x":x_cord,"y":y_cord})
    inner = data.x + data.y + np.power(data.x,2) + np.power(data.y,2) -1
    data1 = data[np.abs(inner) < 2*10**-3]#由于编程精度问题，没有让约束为x + y + x2+y2 -1 = 0，而是x + y + x2+y2 -1 < 0.002
    fig,ax = plt.subplots()
    ax.scatter(data1.x,data1.y)
    ax.axhline(y=0, color='k') #画y轴
    ax.axvline(x=0, color='k') #画x轴
    plt.show()
    
    

    
    
def main():
    # draw_sin()
    # square_x_function()
    # draw_directly()
    high_order_function()
   
    
    
main()
    
