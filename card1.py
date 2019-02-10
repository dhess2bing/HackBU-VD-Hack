import tkinter
import Hackbu_2019_Scrape_Valentines_Quotes
from PIL import Image
def Start():#goes from menu to card
	name1 = reciever.get()
	name2 = gifter.get()
	welcome1.destroy()
	reciever.destroy()
	welcome2.destroy()
	gifter.destroy()
	go.destroy()
	create1()
def create1():
	with open("valentines-quotes.csv", "r") as file:
		csv_reader = reader(file)
		quote = [row for num,row in enumerate(csv_reader) if num in (rand() % 30)]
	num = rand() % 3
	pngfile = Image.open(num+".png")
	pic = tkinter.Label(top,image=pngfile)
	pic.pack()
	pic.place(x = 275,y = 225)
	text = "To "+name1+"\n\t"+quote+"\nFrom "+name2
	words = tkinter.Label(top,text= text)
	words.pack()
	words.place(x = 275, y = 625)
	another.grid()
def Repeat():
	pic.destroy()
	words.destroy()
	create1()
top = tkinter.Tk()
top.geometry("650x750");
top.resizable(0,0);
back = tkinter.Frame(master=top,bg="white");
back.pack_propagate(0)
back.pack(fill=tkinter.BOTH, expand=1)
pic = tkinter.Label(top,text="Insert Image here")
words = tkinter.Label(top,text="Insert quote here")
another = tkinter.Button(master = back, text="Repeat", command=Repeat)
another.grid(row=1,column=0)
pic.destroy()
words.destroy()
another.grid_remove()
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
go = tkinter.Button(top,text="Generate", command=Start)
go.pack()
go.place(x = 275, y = 350)

top.mainloop()
