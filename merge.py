import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('skyrim pricing')
root.geometry('300x550')

can = Canvas(root, width=300, height=550, background='white')
can.pack()



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
# labelc = Label(root, text=concat).pack()

root.mainloop()