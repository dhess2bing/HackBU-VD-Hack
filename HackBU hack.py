import tkinter
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

bottomframe = tkinter.Frame(root)


redbutton = tkinter.Button(frame, text="Red", fg="red", bd = 5, font ="Times")
redbutton.grid()
greenbutton = tkinter.Button(frame, text="Brown", fg="brown", font = "Times")
greenbutton.grid()

bluebutton = tkinter.Button(frame, text="Blue", fg="blue", font = "Times", height = 2)
bluebutton.grid()
blackbutton = tkinter.Button(bottomframe, text="Black", fg="black")
blackbutton.grid()
root.mainloop()
