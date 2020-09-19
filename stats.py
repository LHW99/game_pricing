from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Game Price Stats")
root.geometry('600x600')

# a dropdown box
options = [
  '1',
  '2',
  '3',
  '4'
]

btn=Button(root, text="click here")
btn.pack()

root.mainloop()