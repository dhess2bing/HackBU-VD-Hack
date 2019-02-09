import tkinter
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

bottomframe = tkinter.Frame(root)


redbutton = tkinter.Button(frame, text="Red", fg="red")
redbutton.grid()
greenbutton = tkinter.Button(frame, text="Brown", fg="brown")
greenbutton.grid()

bluebutton = tkinter.Button(frame, text="Blue", fg="blue")
bluebutton.grid()
blackbutton = tkinter.Button(bottomframe, text="Black", fg="black")
blackbutton.grid()
root.mainloop()
