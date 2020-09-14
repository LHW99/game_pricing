from tkinter import *
import pandas as pd
import datetime
import csv
# import matplotlib to graph
import matplotlib.pyplot as plt
from numpy import *

root = Tk()
root.title("line chart")
root.geometry("400x400")

# tried graphing method
"""
# make graph
def graph():
  with open('new.csv', 'r') as file:
    plot = pd.read_csv(file, delimiter=',')

  plt.hist(plot, 20)
  plt.show

# button to populate 
btn = Button(root, text='graph', command=graph)
btn.pack()

root.mainloop()
"""


#tried plt
"""
with open ('new.csv', 'r') as file:
  plot=pd.read_csv(file, delimiter=',')

plt.xlabel('x')
plt.ylabel('y')
plt.title('testing')
plt.plot(plot)
plt.show()
"""

# trying pandas/numpy
headers = ['DateTime', 'Final price']
df = pd.read_csv('new.csv', parse_dates = {"Datetime" : [1,2]}, names=headers)
print (df)

df.plot(x='DateTime', y='Final price')
plt.title('title')
plt.xticks(xValues)
plt.show()