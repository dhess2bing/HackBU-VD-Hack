import tkinter
import tkinter.messagebox

def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    grid_frame = tkinter.Frame(root)
    grid_frame.grid()
    frame.grid()
    
    root.geometry("500x400+400+150")
    bottomframe = tkinter.Frame(root)

    vd_str = "Valentine's Day Card Generator"
    title_label = tkinter.Label(frame, text = vd_str )
    title_label.grid(row = 0, column = 3)

    from_str = ("Who is sending this card? ")
    from_label = tkinter.Label(frame, text = from_str)
    from_label.grid(row = 2, column =2)

    entry_from_str = tkinter.Entry(frame, bd =4)
    entry_from_str.grid(row = 2, column = 3)
    
    
    redbutton = tkinter.Button(frame, text="Generate Card", fg="red", bd = 5, font ="Times")
    redbutton.grid(row = 25, column = 3, rowspan = 15)
    

    root.mainloop()

main()
