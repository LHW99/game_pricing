import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os

root = Tk()
root.title('skyrim pricing')


# reading csv files for skyrim's pricing
a1 = pd.read_csv('price-history-for-72850.csv')
a2 = pd.read_csv('price-history-for-489830.csv')

concat = pd.concat([a1, a2])


# displaying two separate csv files
label1 = Label(root, text=concat).grid(row=0, column=0)
#label2 = Label(root, text=a2).grid(row=0, column=1)

root.mainloop()