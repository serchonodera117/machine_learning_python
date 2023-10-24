# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:19:31 2023
"""
import matplotlib.pyplot as plt
#define data

def setLinearGraphics():
    x1 = [5,4,5,6]
    y1 = [23,23,5,2]
    x2 = [0,3,4,21]
    y2 = [1,2,4,5]
#Seting graphic features
    plt.plot(x1,y1, label = 'Linea 1', linewidth = 4, color='blue')
    plt.plot(x2,y2, label = 'Linea 2', linewidth = 4, color='green')
 #define title and name of axis
    plt.title('Line diagram')
    plt.ylabel('Axis Y')
    plt.xlabel('Axis X')

#show grid, legend and shape
    plt.legend()
    plt.grid()
    plt.show()
    

def graphicBar():
    x1 = [5,4,4,4,8]
    y1 = [2,1,23,5,2]
    x2 = [0,3,4,21,7]
    y2 = [1,2,4,5.7]
    
    #Seting graphic features
    plt.bar(x1,y1, label = 'Data 1', linewidth = 4, color='Lightblue')
    plt.bar(x2,y2, label = 'Data 2', linewidth = 4, color='Orange')
   #define title and name of axis
    plt.title('Line diagram')
    plt.ylabel('Eje Y')
    plt.xlabel('Eje X')

   #show grid, legend and shape
    plt.legend()
    plt.grid()
    plt.show()

def histogram():
    #define data
    a = [22,55,64,21,34,54,23,3,2,4,102,85.85,119,129,79,65,55,111,115,89,75,65,44,443,42,48]
    bins = [0,10,20,30,40,50,70,80,90,100]
    #seting features of graphic
    plt.hist(a, bins, histtype='bar', rwidth = 0.8, color='lightgreen')
    #Define title, name and axis
    plt.title('histogram')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()
    

def dispersionGraphic():
    x1 = [0.25, 1.25,2.25,3.25, 4.35]
    y1 = [10,55,80,32,40]
    x2 = [0.75, 1.75,2.75, 3.75,4.75]
    y2 = [42, 26, 10, 29, 66]
    #set features of graphic
    plt.scatter(x1, y1, label = 'data 1', color = 'red')
    plt.scatter(x2, y2, label = 'data 2', color = 'purple')
    
    #define title and axis name
    plt.title('graphic of dispersion')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    #show shape
    plt.legend()
    plt.show()

def cicleGraphics():
    sleep = [7,8,6,11,7]
    eat =   [2,3,4,3,2]
    work =  [7,8,2,2,5]
    divide = [7,2,2,13]
    reacration = [8,5,7,8,13]
    activity = ['sleep', 'eat', 'work', 'recreation']
    myColors = ['red', 'purple', 'blue', 'orange']
    
    plt.pie(divide, labels=activity, colors=myColors, startangle=90,
            shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%')
    plt.title('cicle graphic')
    plt.show()
    
#setLinearGraphics()
#graphicBar()
#histogram()
#dispersionGraphic()
cicleGraphics()