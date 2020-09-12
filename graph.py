from tkinter import *
import pandas as pd
import csv
import matplotlib.pyplot as plt

root = Tk()
root.title("line chart")
root.geometry("400x400")


def graph():
  with open('new.csv', 'r') as file:
    plot = csv.reader(file, delimiter=',')

    plt.hist(plot)
    plt.show

btn = Button(root, text='graph', command=graph)
btn.pack()


root.mainloop()