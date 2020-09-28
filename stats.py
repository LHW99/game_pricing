from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from numpy import *
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

root = Tk()
root.title("Game Price Stats")
root.geometry('300x150')

# selections for dropdown
options = [
  'Graph',
  'Regular/Sales Prices',
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
  for line in df['Final price']:
    if line > reg_price:
      reg_price = line
  return reg_price

# command to find lowest sale price of game
def l_price():
  low_price = 99.99
  for line in df['Final price']:
    if line < low_price:
      low_price = line
  return low_price

# command to find the latest date in the csv file
def latest_date():
  last_date = df['DateTime'].iloc[-1]
  date_time_obj = datetime.strptime(last_date, '%Y-%m-%d %H:%M:%S')
  last_date2 = date_time_obj.date()
  return last_date2

# calculate the year before the latest date
def year_before():
  sales = 0
  last_year = latest_date() - relativedelta(years=1)
  return last_year
  """
  reg_price = r_price()

  # make a new data frame??
  for line in df['DateTime']
    if datetime.strptime(line, '%Y-%m-%d %H:%M:%S').date() > last_year:
      sales+=1

  return sales
  """
# calculate the month before the latest date
def month_before():
  last_month = latest_date() - relativedelta(months=1)
  return last_month

def new_df():
  last_year = pd.to_datetime(year_before())
  reg_price = r_price()
  df['DateTime'] = pd.to_datetime(df.DateTime)

  ndf = df[(df['DateTime'] > last_year) & (df['Final price'] < reg_price)]
  return ndf

# command to select how to manipulate csv
def select():
  top=Toplevel()
  # if user has not selected a csv file
  if lb_file.cget("text") == "Selected File: ":
    lb = Label(top, text="Please select a csv file").pack(pady=10, padx=10)
  # if user selects options
  elif clicked.get() == 'Graph':
    graph().pack()
  elif clicked.get() == 'Regular/Sales Prices':
    top.title('Regular/Sales Prices')
    top.geometry('300x300')
    lb = Label(top, text='Regular Price: '
     + str(r_price()) 
     + '\nLowest Price: ' 
     + str(l_price())
     + '\nLargest Discount: '
     + str(int(l_price() / r_price() * 100))
     + '%').pack()
  elif clicked.get() == '3':
    top.title('second window')
    top.geometry('300x300')
    lb = Label(top, text= str(year_before())).pack()
  elif clicked.get() == '4':
    top.title('second window')
    top.geometry('300x300')
    lb = Label(top, text=str(new_df())).pack()

# button to execute from dropdown
ex_btn=Button(root, text="execute", command=select)
ex_btn.pack()

# button to find file
op_btn=Button(root, text="open file", command=open)
op_btn.pack()

root.mainloop()