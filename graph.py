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
# skyrim price history
"""
df = pd.read_csv('new.csv',header=0,parse_dates=True,infer_datetime_format=True)
print (df)
"""

df1 = pd.read_csv('price-history-for-489830.csv', header=0, parse_dates=True,infer_datetime_format=True)
df2 = pd.read_csv('price-history-for-72850.csv', header=0, parse_dates=True,infer_datetime_format=True)

ff = plt.figure(figsize=(30,10))
fig, axes = plt.subplots()

df1.plot(ax=axes[0,0])
df2.plot(ax=axes[0,1])

plt.title('Skyrim Pricing')
plt.show()