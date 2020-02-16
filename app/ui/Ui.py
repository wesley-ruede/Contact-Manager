import builtins
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
label = tkinter.Label(frame, text="Hello, World")
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
message = tkinter.Message(frame,text="A message")

label.pack(fill=X, expand=1)
frame.pack(fill=BOTH,expand=1)
button.pack(side=BOTTOM)

tk.mainloop()
