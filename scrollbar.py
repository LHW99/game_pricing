from tkinter import *
from tkinter import ttk

root=Tk()

main_frame=Frame(root)
main_frame.pack()

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = mycanvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(100):
  Button(second_frame, text=f'Button {thing}').grid(row=thing,column=0,pady=10,padx=10)

root.mainloop()