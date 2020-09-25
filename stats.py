from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
  root.filename = filedialog.askopenfilename(initialdir='/home/haiduk/python/game_price',
  title='Select a file',
  filetypes=[("csv files", "*.csv")])
  
  global df
  df = pd.read_csv(root.filename,
  header=0,
  parse_dates=True,
  infer_datetime_format=True,
  delimiter=',')

  # clears existing file if selected, and shows selected file
  lb_file.pack_forget()
  lb_file = Label(root, text="Selected File: " + root.filename)
  lb_file.pack()

# graph
def graph():
  x,y = df['DateTime'],df['Final price']
  plt.plot(x,y)

  # labels & title
  plt.title('Price over Time')
  plt.xticks(rotation=65)
  plt.xlabel("Date")
  plt.ylabel("Price")

  # change formatting to remove times on x-axis
  plt.xlabel.set_major_formatter(mdates.DateFormatter("%Y-%m"))
  plt.show()

# command to select how to manipulate csv
def select():
  top=Toplevel()
  if clicked.get() == 'Graph':
    graph().pack
  elif clicked.get() == '2':
    top.title('second window')
    top.geometry('300x300')
    lb = Label(top, text='test2').pack()
  elif clicked.get() == '3':
    top.title('second window')
    top.geometry('300x300')
    lb = Label(top, text='test3').pack()
  elif clicked.get() == '4':
    top.title('second window')
    top.geometry('300x300')
    lb = Label(top, text='test4').pack()

# button to execute from dropdown
ex_btn=Button(root, text="execute", command=select)
ex_btn.pack()

# button to find file
op_btn=Button(root, text="open file", command=open)
op_btn.pack()

# label for selected file
global lb_file
lb_file = Label(root, text="Selected File: ")
lb_file.pack()

root.mainloop()