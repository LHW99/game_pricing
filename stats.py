from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Game Price Stats")
root.geometry('600x600')

dat = ""

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

global lb
lb = Label(root, text='').pack()

def select():
  if clicked.get() == '1':
    lb.destroy()
    lb = Label(root, text='test1').pack()
  elif clicked.get() == '2':
    lb.destroy()
    lb = Label(root, text='test2').pack()
  elif clicked.get() == '3':
    lb.destroy()
    lb = Label(root, text='test3').pack()
  elif clicked.get() == '4':
    lb.destroy()
    lb = Label(root, text='test4').pack()


# button to execute
btn=Button(root, text="click here", command=select)
btn.pack()

root.mainloop()