from tkinter import *
import pandas as pd
import datetime
import csv
# import matplotlib to graph
import matplotlib.pyplot as plt
from numpy import *
from glob import glob

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

"""
ff = plt.figure(figsize=(30,10))
subplots(1 row, 1 column); how many subplots will be in the figure (f)
f, axes = plt.subplots(1, 1)
ax10 = ff.add_subplot()
ax10.plot(df1)
ax10.plot(df2)
"""

files = glob('test*.csv')

for file in files:
  name = file.split('test*.csv')[0]
  df = pd.read_csv(file, header=0, parse_dates=True,infer_datetime_format=True,delimiter=',')

  x,y = df['DateTime'],df['Final price']

  fig, ax=plt.subplots(figsize=(7,4))

  ax.plot(x,y)

  plt.tight_layout()
  plt.savefig(name+'.png', dpi=300, bbox='tight')

plt.title('Skyrim Pricing')
plt.show()