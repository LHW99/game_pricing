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
import csv

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

root = Tk()
root.title("Game Price Stats")
root.geometry('450x150')

# selections for dropdown
options = [
  'Graph',
  'Regular/Sales Prices',
  'No. of Sales in Past Year',
  'No. of Sales in Past Month'
]

clicked = StringVar()
clicked.set(options[0])

# a dropdown box
drop = OptionMenu(root, clicked, *options)
drop.config(width=22, anchor='w', justify=LEFT)
drop.grid(column=1,row=1, padx=(15,0), sticky='w')

# label for selected file
lb_file = Label(root, text="Dummy data loaded.\nGive it a try!", justify=LEFT, width=22, anchor='w')
lb_file.grid(column=1,row=0, pady=(35,15), padx=(15,0), sticky='w')

# dummy data example
df = pd.read_csv('dummy.csv',
  header=0,
  parse_dates=True,
  infer_datetime_format=True,
  delimiter=',')

# command to find a file
def open():
  root.filename = filedialog.askopenfilename(initialdir='/',
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
  lb_file = Label(root, text="File:\n" + root.filename, justify=LEFT, anchor='w')
  lb_file.grid(column=1,row=0, pady=(35,15), padx=(15,0), sticky='w')

# graph
def graph():
  # create figure
  fig, ax = plt.subplots(figsize=(8, 8))

  # convert date/time to matplotlib readable format
  altered_dates = pd.to_datetime(df['DateTime'])
  df['mdate'] = [mdates.date2num(d) for d in altered_dates]

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
  last_year = latest_date() - relativedelta(years=1)
  return last_year

# calculate the month before the latest date
def month_before():
  last_month = latest_date() - relativedelta(months=1)
  return last_month

# calculates number of sales in past year from latest date
def new_dfy():
  last_year = pd.to_datetime(year_before())
  reg_price = r_price()
  filtered_year = pd.to_datetime(df.DateTime)

  ndf = df[(filtered_year > last_year) & (df['Final price'] < reg_price)]
  
  sales_y = ndf['Final price'].count()

  return "No. of sales in year\nprior to " + str(latest_date()) + ": " + str(sales_y)

# calculates number of sales in past month from latest date
def new_dfm():
  last_month = pd.to_datetime(month_before())
  reg_price = r_price()
  filtered_month = pd.to_datetime(df.DateTime)

  mdf = df[(filtered_month > last_month) & (df['Final price'] < reg_price)]
  
  sales_m = mdf['Final price'].count()

  return "No. of sales in month\nprior to " + str(latest_date()) + ": " + str(sales_m)

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
    top.geometry('300x70')
    lb = Label(top, text='Regular Price: '
     + str(r_price()) 
     + '\nLowest Price: ' 
     + str(l_price())
     + '\nLargest Discount: '
     + str(int(l_price() / r_price() * 100))
     + '%').pack()
  elif clicked.get() == 'No. of Sales in Past Year':
    top.title('Sales in Past Year')
    top.geometry('300x70')
    lb = Label(top, text= str(new_dfy())).pack()
  elif clicked.get() == 'No. of Sales in Past Month':
    top.title('Sales in Past Month')
    top.geometry('300x70')
    lb = Label(top, text=str(new_dfm())).pack()

# button to execute from dropdown
ex_btn=Button(root, text="Execute", command=select, width=15)
ex_btn.grid(column=0,row=1, padx=(30,10))

# button to find file
op_btn=Button(root, text="Open File", command=open, width=15)
op_btn.grid(column=0,row=0, padx=(30,10), pady=(30,10))

root.mainloop()