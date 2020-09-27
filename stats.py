from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from numpy import *

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

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

# label for selected file
lb_file = Label(root, text="Selected File: ")
lb_file.pack()

# command to find a file
def open():
  root.filename = filedialog.askopenfilename(initialdir='/home/haiduk/python/game_price',
  title='Select a file',
  filetypes=[("csv files", "*.csv")])
  
  # csv reader
  global df
  df = pd.read_csv(root.filename,
  header=0,
  parse_dates=True,
  infer_datetime_format=True,
  delimiter=',')

  # clears existing file label if selected, and shows selected file
  global lb_file
  lb_file.pack_forget()
  lb_file = Label(root, text="Selected File: " + root.filename)
  lb_file.pack()

# graph
def graph():
  # create figure
  fig, ax = plt.subplots(figsize=(8, 8))

  # convert date/time to matplotlib readable format
  df['DateTime'] = pd.to_datetime(df['DateTime'])
  df['mdate'] = [mdates.date2num(d) for d in df['DateTime']]

  # x and y values for graph
  ax.plot(df['mdate'], df['Final price'])

  # labels
  ax.set(xlabel="Date", ylabel="Price", title = "Price over Time")

  # clean date format
  date_form = DateFormatter("%Y-%m-%d")
  ax.xaxis.set_major_formatter(date_form)

  # rotate x-axis labels
  plt.xticks(rotation = 65)

  plt.show()

# command to find regular price of game
def r_price():
  reg_price = 0.0
  for line in df['Final price']

# command to find lowest sale price of game
def l_price ():
  low_prices = 0.0
  for line in df['Final price']

# command to select how to manipulate csv
def select():
  top=Toplevel()
  if clicked.get() == 'Graph':
    graph().pack()
  elif clicked.get() == 'Regular/Sales Prices':
    top.title('Regular/Sales Prices')
    top.geometry('300x300')
    lb = Label(top, text='place holder').pack()
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



root.mainloop()