import tkinter
import tkinter.messagebox

def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    frame.pack()
    bottomframe = tkinter.Frame(root)
    bluebutton = tkinter.Button(frame, text="Blue", fg="blue", font = "Times", height = 2)
    bluebutton.grid()
    blackbutton = tkinter.Button(bottomframe, text="Black", fg="black")
    blackbutton.grid()
    root.mainloop()
