from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from numpy import *

root = Tk()
root.title("Game Price Stats")
root.geometry('300x150')

# selections for dropdown
options = [
  'Graph',
  '2',
  '3',
  '4'
]

clicked = StringVar()
clicked.set(options[0])

# a dropdown box
drop = OptionMenu(root, clicked, *options)
drop.pack()

# command to find a file
def open():
  root.filename = filedialog.askopenfilename(initialdir='/',
  title='Select a file',
  filetypes=[("csv files", "*.csv")])
  
  global df
  df = pd.read_csv(root.filename,
  header=0,
  parse_dates=True,
  infer_datetime_format=True,
  delimiter=',')

# graph
def graph():
  plt.plot(df)
  plt.title('test title')
  plt.show()

# command to select how to manipulate csv
def select():
  top=Toplevel()
  top.title('second window')
  top.geometry('300x300')
  if clicked.get() == 'Graph':
    lb = Label(top, text=graph()).pack()
  elif clicked.get() == '2':
    lb = Label(top, text='test2').pack()
  elif clicked.get() == '3':
    lb = Label(top, text='test3').pack()
  elif clicked.get() == '4':
    lb = Label(top, text='test4').pack()

# button to execute from dropdown
ex_btn=Button(root, text="execute", command=select)
ex_btn.pack()

# button to find file
op_btn=Button(root, text="open file", command=open)
op_btn.pack()

root.mainloop()