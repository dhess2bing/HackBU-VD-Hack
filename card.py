import tkinter

def Start():#goes from menu to card
    name1 = reciever.get()
    name2 = gifter.get()
    welcome1.grid_remove()
    reciever.grid_remove()
    welcome2.grid_remove()
    gifter.grid_remove()
    create1()
def create1():
    pic = tkinter.Label(top,text="Insert Image here")
    pic.pack()
    pic.place(x = 275,y = 250)
    words = tkinter.Message(top,pady=3,text="Insert quote here")
    words.pack()
    words.place(x = 275, y = 625)
def Repeat(pic):
    pic.grid_remove()
    #create1()
def Return():#goes back to menu
    pic.lower()
    words.lower()
    another.grid_remove()
    welcome1.pack()
    reciever.pack()
    welcome2.pack()
    gifter.pack()
    go.pack()
top = tkinter.Tk()
top.geometry("650x750");
top.resizable(0,0);
back = tkinter.Frame(master=top,bg="light pink");
back.pack_propagate(0)
back.pack(fill=tkinter.BOTH, expand=1)
name1 = "";
name2 = "";
welcome1 = tkinter.Label(top,text="Insert the Recipient's name here")
welcome1.pack()
welcome1.place(x = 275, y = 250)
reciever = tkinter.Entry(top)
reciever.pack()
reciever.place(x = 275, y = 275)
welcome2 = tkinter.Label(top,text="Insert the Sender's name here")
welcome2.pack()
welcome2.place(x = 275, y = 300)
gifter = tkinter.Entry(top)
gifter.pack()
gifter.place(x = 275, y = 325)
go = tkinter.Button(top,text="Generate", command=Start())
go.pack()
go.place(x = 275, y = 350)
pic = tkinter.Label(top,text="Insert Image here")
words = tkinter.Message(top,pady=3,text="Insert quote here")
another = tkinter.Button(master = back, text="Repeat", command=Repeat(pic))
another.grid(row=0,column=0)
another.destroy()

top.mainloop()

