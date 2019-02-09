import tkinter
import tkinter.messagebox

def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    frame.pack()
    root.geometry("500x400+400+150")
    bottomframe = tkinter.Frame(root)

    vd_str = "Valentine's Day Card Generator"
    title_label = tkinter.Label(frame, text = vd_str )
    title_label.pack(side = tkinter.TOP)
    
    redbutton = tkinter.Button(frame, text="Red", fg="red", bd = 5, font ="Times")
    redbutton.pack(side = tkinter.TOP)

    
    greenbutton = tkinter.Button(frame, text="Brown", fg="brown", font = "Times")
    greenbutton.pack(side = tkinter.TOP)


    

    root.mainloop()

main()
