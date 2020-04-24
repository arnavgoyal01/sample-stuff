import matplotlib.pyplot as plt 
import numpy as np
'''
#Line Graph 
x= [1,2,5]
y= [2,3,7]
x1=[8,9,10]
y1=[7,9,6]
plt.plot(x, y, label= "First Line")
plt.plot(x1, y1, label="Second Line")
plt.ylabel("YYYYY")
plt.xlabel("XXXXX")
plt.title("Title")
plt.legend()

#Bar Graph 
plt.bar([1,2,3,4], [2,5,7,9], label= "Example 1")
plt.bar([5,6,7,8],[1,4,2,7], label="Example 2")
plt.title("Title 2")
plt.ylabel("Y2Y2Y2Y2")
plt.xlabel("X2X2X2X2")
plt.legend()


#Histogram 
var1= [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
var2 = bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(var1, var2, histtype = "bar", rwidth= 0.3)
plt.xlabel("X3X3X3X3")
plt.ylabel("Y2Y2Y2")
plt.title("Histogram")
plt.legend()

#Scatter Plot 
x = [1,4,2,5,3,7,5,8,6,9,4]
y = [4,2,4,6,8,6,4,5,7,9,1]
plt.scatter(x, y, label = "skitscat", color = "k", s=50, marker="o")
plt.xlabel("X3X3X3X3")
plt.ylabel("Y3Y2Y2")
plt.title("Scatter Plot")
plt.legend()

#Stackplot 
days= [1, 2, 3, 4, 5]
sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
plt.plot([], [], color = "m", label= "Sleeping", linewidth= 5)#Line 48-51 create a legend on the stackplot graph
plt.plot([], [], color = "c", label= "Eating", linewidth= 5)
plt.plot([], [], color = "r", label= "Working", linewidth= 5)
plt.plot([], [], color = "k", label= "Playing", linewidth= 5)
plt.stackplot(days, sleeping, eating, working, playing, colors = ["m", "c", "r", "k"])
plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Stackplot")

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=60,#Angle of the starting line from 0 degrees, slices are arranged in anti-clockwise manner      
        shadow= True,
        explode=(0,0.5,0,0),# Seperates certain slices from the pie, number signifies how big the seperation is 
        autopct='%1.1f%%')#Code to overlap the labels on top of the slices 

plt.title('Interesting Graph\nCheck it out')

#Getting Data from File 
import numpy as np
x, y = np.loadtxt('sample.txt', delimiter=',', unpack=True)
plt.plot(x, y, label="Loaded from sample.txt")
plt.xlabel("Something")
plt.ylabel("SomethingX2")
plt.title("How to extract data from exxternal file(sample.txt)")
plt.legend()
'''

plt.show()
