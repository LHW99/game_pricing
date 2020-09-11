import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import csv


root = Tk()
root.title('skyrim pricing')
root.geometry('500x550')

# making a main frame
fra = Frame(root)
fra.pack(fill=BOTH, expand=1)

# making a canvas for the scroll bar
can = Canvas(fra)
can.pack(side=LEFT, fill=BOTH, expand=1)

# making a scroll bar
sb = Scrollbar(fra, orient=VERTICAL, command=can.yview)
sb.pack(side=RIGHT, fill=Y)

# configure canvas; when we scroll, we want something to happen
can.configure(yscrollcommand=sb.set)
# bbox is a bounding box; ie scroll the entire box
# binds configure to an event (lambda e)
can.bind('<Configure>', lambda e: can.configure(scrollregion=can.bbox("all")))

# create second frame inside canvas
fra2 = Frame(can)

# new frame to a window in the canvas
can.create_window((0,0), window=fra2, anchor="nw")

# to prevent truncating the rows for large data set, set max_rows to None
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

# reading csv files for skyrim's pricing
a1 = pd.read_csv('price-history-for-72850.csv')
a2 = pd.read_csv('price-history-for-489830.csv')

# concatenating both csv files with pandas
concat = pd.concat([a1, a2], ignore_index=True)

# displaying two separate csv files
#label1 = Label(root, text=a1).grid(row=0, column=0)
#label2 = Label(root, text=a2).grid(row=0, column=1)

# displaying the concat csv
labelc = Label(fra2, text=concat).grid()

# writing a new csv file
with open('new.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  for line in concat:
    writer.writerows(line)

root.mainloop()