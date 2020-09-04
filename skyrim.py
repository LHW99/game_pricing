import pandas as pd
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('skyrim pricing')

df = pd.read_csv('price-history-for-72850.csv')

label = Label(root, text=df).pack()

root.mainloop()