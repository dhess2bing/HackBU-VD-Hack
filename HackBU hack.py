import tkinter
import tkinter.messagebox

def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    frame.pack()

    bottomframe = tkinter.Frame(root)

    title_text = tkinter.Text(frame, font = "Times")
    redbutton = tkinter.Button(frame, text="Red", fg="red", bd = 5, font ="Times")
    redbutton.pack(side = "left")
    greenbutton = tkinter.Button(frame, text="Brown", fg="brown", font = "Times")
    greenbutton.pack(side = "bottom")




    """
    bluebutton = tkinter.Button(frame, text="Blue", fg="blue", font = "Times", height = 2)
    bluebutton.grid()
    blackbutton = tkinter.Button(bottomframe, text="Black", fg="black")
    blackbutton.grid()
    """
    root.mainloop()
