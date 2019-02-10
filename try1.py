import tkinter as tk
from PIL import Image
import random

NUMBER_OF_IMAGES = 3

window = Tkinter.Tk()

window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

pic_number = random.randrange(1,4)
path = ("%s.jpg" %s, pic_number)

img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()
