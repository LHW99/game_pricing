from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Game Price Stats")
root.geometry('300x150')

# selections for dropdown
options = [
  '1',
  '2',
  '3',
  '4'
]

clicked = StringVar()
clicked.set(options[0])

# a dropdown box
drop = OptionMenu(root, clicked, *options)
drop.pack()

def select():
  top=Toplevel()
  top.title('second window')
  top.geometry('300x300')
  if clicked.get() == '1':
    lb = Label(top, text='test1').pack()
  elif clicked.get() == '2':
    lb = Label(top, text='test2').pack()
  elif clicked.get() == '3':
    lb = Label(top, text='test3').pack()
  elif clicked.get() == '4':
    lb = Label(top, text='test4').pack()


# button to execute
btn=Button(root, text="click here", command=select)
btn.pack()

root.mainloop()